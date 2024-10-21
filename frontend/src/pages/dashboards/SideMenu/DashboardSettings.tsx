import { useState } from "react";
import { Button, Modal } from "react-bootstrap";
import { useToggle } from "../../../hooks";
import FormInput from "../../../components/form/FormInput";
import { MenuItem } from "react-pro-sidebar";
import { useDispatch } from "react-redux";
import { setRefreshTime } from "../../../redux/actions";
import LiveDataToggle from "./LiveDataToggle";

function DashboardSettings() {
  const [isOpen, show, hide] = useToggle();
  const [selectedOption, setSelectedOption] = useState("1dk");

  const dispatch = useDispatch();

  const toggleExportModal = () => {
    isOpen ? hide() : show();
  };
  const handleRefreshTime = (refreshInterval: number) => {
    dispatch(setRefreshTime(refreshInterval));
  };
  const handleSelectChange = (event: any) => {
    setSelectedOption(event.target.value);
  };

  const handleSaveSettings = () => {
    let refreshInterval: number;
    switch (selectedOption) {
      case "10sn":
        refreshInterval = 1 * 10 * 1000;
        handleRefreshTime(refreshInterval);
        break;
      case "1dk":
        refreshInterval = 1 * 60 * 1000;
        handleRefreshTime(refreshInterval);
        break;
      case "5dk":
        refreshInterval = 5 * 60 * 1000;
        handleRefreshTime(refreshInterval);

        break;
      case "15dk":
        refreshInterval = 15 * 60 * 1000;
        handleRefreshTime(refreshInterval);

        break;
      default:
        console.log(`invalid refresh interval: ${selectedOption}`);
        break;
    }

    hide();
  };

  return (
    <div
      style={{
        padding: 0,
        margin: 0,
        height: 10,
      }}
    >
      <MenuItem onClick={toggleExportModal} style={MenuItemStyle}>
        Panel Ayarları
      </MenuItem>
      <Modal show={isOpen} onHide={toggleExportModal} centered>
        <Modal.Header closeButton>
          <h4 className="modal-title"> Panel Ayarları</h4>
        </Modal.Header>
        <Modal.Body
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column",
          }}
        >
          <LiveDataToggle />
          <FormInput
            name="select"
            label="Veri Yenileme Sıklığı:"
            type="select"
            containerClass="mb-1"
            className="form-select"
            key="select"
            onChange={handleSelectChange}
            value={selectedOption}
          >
            <option value="10sn">10 saniye</option>
            <option value="1dk">1 dakika</option>
            <option value="5dk">5 dakika</option>
            <option value="15dk">15 dakika</option>
          </FormInput>
        </Modal.Body>
        <Modal.Footer
          style={{
            display: "flex",
            justifyContent: "center",
            padding: 30,
            marginTop: 10,
          }}
        >
          <Button
            style={{
              borderRadius: 30,
              width: 250,
            }}
            onClick={handleSaveSettings}
          >
            Kaydet
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default DashboardSettings;

const MenuItemStyle = {
  margin: 0,
  height: 10,
  backgroundColor: "#323a46",
  fontSize: 16,
  fontWeight: 500,
  color: "#fcf8e3",
};
