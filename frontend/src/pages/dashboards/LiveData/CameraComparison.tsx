import { useEffect, useState } from "react";
import { Card, ProgressBar } from "react-bootstrap";
import { formatDate } from "../../../utils/helpers";
import { CameraItem } from "../../camera-setup/types";
import config from "../../../config";
import { useSelector } from "react-redux";
import { fetchCamsData, getAllCameras } from "../../../utils/api/apis";
import { CameraCount } from "../types";

//ignored from list and calculation
// const ignoredCamLabel = "Giriş";

const CameraComparison = () => {
  const [cameras, setCameras] = useState<CameraItem[]>([]);
  const [cameraCounts, setCameraCounts] = useState<CameraCount[]>([]);
  const refreshTime = useSelector((state: any) => state.Dashboard.refreshTime);

  const totalCustomersCount = cameraCounts.reduce(
    (total, cam) => total + cam.count,
    0
  );

  const cameraCustomerRatios = cameraCounts.map((cam) => ({
    label: cam.label,
    count: cam.count,
    ratio: (cam.count / totalCustomersCount) * 100,
  }));

  const colors = ["danger", "info", "warning", "success"];

  cameraCustomerRatios.sort((a, b) => b.ratio - a.ratio);

  //for requests
  let startDate = new Date();
  startDate.setHours(config.workingHoursStart, 0, 0, 0);
  let start_date = formatDate(startDate);

  let endDate = new Date();
  endDate.setHours(config.workingHoursEnd, 0, 0, 0);
  let end_date = formatDate(endDate);

  useEffect(() => {
    getAllCameras().then(setCameras);
  }, []);

  useEffect(() => {
    if (cameras.length > 0) {
      fetchCamsData(cameras, start_date, end_date).then((data) => {
        setCameraCounts(data);
      });

      const intervalId = setInterval(() => {
        fetchCamsData(cameras, start_date, end_date).then((data) => {
          setCameraCounts(data);
        });
      }, refreshTime);

      return () => clearInterval(intervalId);
    }
  }, [cameras]);

  return (
    <Card>
      <Card.Body className="h-48" style={{ height: 362 }}>
        <h4 className="header-title">Kamera Karşılaştırması</h4>
        <p className="sub-header">
          Kameralara Göre <b>müşteri</b> sayıları oranları
        </p>
        {cameraCustomerRatios.map((cam, index) => (
          <div key={index}>
            <div className="d-flex justify-content-between">
              <p className="sub-header p-0 m-0 text-start">{cam.label}</p>
              <p className="sub-header p-0 m-0 text-end">
                {cam.count}
                {/* ({cam.ratio.toFixed(2)}%) */}
              </p>
            </div>
            <ProgressBar
              now={cam.ratio}
              className="m-0 p-0 mt-1 mb-2"
              variant={colors[index % colors.length]}
            />
          </div>
        ))}
      </Card.Body>
    </Card>
  );
};

export default CameraComparison;
