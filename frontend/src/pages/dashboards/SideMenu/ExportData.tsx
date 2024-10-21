import React, { useState } from "react";
import { Button, Col, Form, Modal, Row } from "react-bootstrap";
import AdmintoDatepicker from "../../../components/Datepicker";
import { format } from "date-fns";
import "react-modern-calendar-datepicker/lib/DatePicker.css";
import config from "../../../config";

function ExportData() {
  const [exportModal, setExportModal] = useState<boolean>(false);
  const [startDate, setStartDate] = useState<Date>(new Date());
  const [endDate, setEndDate] = useState<Date>(new Date());
  const [loading, setLoading] = useState(false);
  const [downloadUrl, setDownloadUrl] = useState<string | null>(null);
  const [exportOption, setExportOption] = useState("pdf");

  const exportUrl = config.SERVICE_URL;
  const url = `${exportUrl}/api/export/${exportOption}`;
  // const modules = ["module1", "module2", "module3"];

  const branch_id = config.branchId;

  const formattedStartDate = format(startDate, "yyyy-MM-dd HH:mm:ss.SS+00");
  const formattedEndDate = format(endDate, "yyyy-MM-dd HH:mm:ss.SS+00");

  const toggleExportModal = () => {
    setExportModal((prevstate) => !prevstate);
  };

  const onDateChange = (date: Date, isStart: boolean) => {
    if (date && isStart) {
      setStartDate(date);
    }
    if (date && !isStart) {
      setEndDate(date);
    }
  };

  const handleExportOption = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setExportOption(event.target.value);
  };

  const requestBody = {
    branch_id: branch_id,
    // modules: modules,
    between: {
      start_date: formattedStartDate,
      end_date: formattedEndDate,
    },
    // data_name: {
    //   file_type: exportOption,
    //   folder_name: "report",
    //   file_name: "demo2",
    // },
  };

  const handleDownload = async () => {
    console.log(
      `istek gönderildi. ${url} startDate:${formattedStartDate}, endDate:${formattedEndDate}`
    );

    setLoading(true);
    let response;
    try {
      // request
      response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestBody),
      });
      // console.log('url export>>>', url)
      // resp
      if (response.ok) {
        const data = await response.json();
        setDownloadUrl(data.url);
        // console.log('dosya hazır. url>>>>', data.url)
      }
    } catch (error) {
      console.error("export csv error:", error);
    }
    setLoading(false);
  };

  // useEffect(() => {
  //   console.log('exportOption changed>>>', exportOption)
  // }, [exportOption])

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
        justifyContent: "center",
        alignItems: "center",
        width: "100%",
        padding: "0.5rem 0px",
        marginTop: 100,

        // margin: '30px 0 30px 18px',
      }}
    >
      <Button
        variant="primary"
        style={{ borderRadius: 15, paddingTop: 10, paddingBottom: 10 }}
        onClick={toggleExportModal}
      >
        Rapor Oluştur
      </Button>
      <Modal show={exportModal} onHide={toggleExportModal} centered>
        <Modal.Header closeButton>
          <h4 className="modal-title">Veri Çıktısı Al</h4>
        </Modal.Header>
        <Modal.Body
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column",
            padding: 60,
          }}
        >
          <div></div>
          <div style={{ textAlign: "center" }}>
            <Row className="mt-1 mb-4">
              <Col xl={12}>
                <h5 style={{ textAlign: "left" }}>Tarih Aralığı Seçiniz</h5>
              </Col>
              <Col xl={6}>
                {/* datepicker */}
                <AdmintoDatepicker
                  showTimeSelect={false}
                  dateFormat="dd-MM-yyyy"
                  value={startDate}
                  maxDate={endDate}
                  onChange={(date: Date) => {
                    onDateChange(date, true);
                  }}
                  locale="tr"
                />
              </Col>
              <Col xl={6}>
                <AdmintoDatepicker
                  showTimeSelect={false}
                  value={endDate}
                  dateFormat="dd-MM-yyyy"
                  minDate={startDate}
                  onChange={(date: Date) => {
                    onDateChange(date, false);
                  }}
                  locale="tr"
                />
              </Col>
            </Row>
            <Row>
              <Col xl={6} style={{ display: "flex", flexDirection: "column" }}>
                <h5 style={{ textAlign: "left" }}>Dosya Türü</h5>
                <Form.Select
                  aria-label="Dosya Türü Seçiniz"
                  onChange={handleExportOption}
                  disabled={downloadUrl ? downloadUrl.length > 0 : false}
                >
                  <option value="pdf">PDF</option>
                  <option value="csv">CSV</option>
                </Form.Select>
              </Col>
            </Row>
          </div>
        </Modal.Body>
        <Modal.Footer
          style={{ display: "flex", justifyContent: "center", padding: 30 }}
        >
          <div>
            {loading ? (
              <p>İndirme Bağlantısı Oluşturuluyor..</p>
            ) : downloadUrl ? (
              <a href={downloadUrl} download>
                <Button
                  variant="success"
                  style={{ borderRadius: 30, width: 250 }}
                >
                  Raporu İndir
                </Button>
              </a>
            ) : (
              <Button
                variant="primary"
                style={{ borderRadius: 30, width: 250 }}
                onClick={handleDownload}
              >
                Raporu Oluştur
              </Button>
            )}
          </div>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default ExportData;
