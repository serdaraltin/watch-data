import { Card } from "react-bootstrap";
import { Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import { Link, useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";

import BranchSearch from "./SideMenu/BranchSearch";
import DashboardSettings from "./SideMenu/DashboardSettings";
import ExportData from "./SideMenu/ExportData";
import LiveDataToggle from "./SideMenu/LiveDataToggle";
import CompanyCard from "./SideMenu/CompanyCard";
import UpgradeSubscription from "./SideMenu/UpgradeSubscription";
import { user } from "../../data/user";
import CurrentDatePicker from "./SideMenu/CurrentDatePicker";

const LeftSideMenu = () => {
  const navigate = useNavigate();

  const selectedCamera = useSelector(
    (state: any) => state.Dashboard.selectedCamera
  );

  return (
    <Card
      style={{
        paddingTop: 30,
        margin: "20px 26px 26px 0px",
        minWidth: "200px",
        minHeight: "600px",
        maxWidth: "200px",
      }}
      className="d-none d-md-block"
    >
      <Menu style={{ paddingTop: 7 }}>
        <CompanyCard user={user} />
        <hr />
        <CurrentDatePicker />
        <hr />
        <DashboardSettings />
        <hr />

        <h4
          style={{
            backgroundColor: "#323a46",
            textAlign: "start",
            paddingLeft: 20,
          }}
        >
          Şubeler
        </h4>
        <div className="search-custom">
          <li
            className="d-lg-block "
            style={{ backgroundColor: "#323a46", border: "white" }}
          >
            <BranchSearch />
          </li>
        </div>
        <div style={{ marginTop: 300 }}>
          {selectedCamera !== "all" && (
            <>
              {/* <MenuItem
                icon={""}
                style={MenuItemStyle}
                onClick={() => navigate("/cameras")}
              >
                Kameralar{" "}
                <span style={{ color: "green" }}>
                  ({user.currentCamCount}/{user.maxCamCount})
                </span>
              </MenuItem> */}
              {/* <MenuItem icon={""} style={MenuItemStyle} onClick={() => {}}>
                Şube Ayarları
              </MenuItem> */}
            </>
          )}
          {/* <SubMenu
              label="Faturalar"
              className="d-lg-block "
              style={{ backgroundColor: '#323a46', color: 'white' }}
            >
            </SubMenu> */}
          {/* <MenuItem icon={''} style={MenuItemStyle} onClick={() => {}}>
              Faturalar{' '}
            </MenuItem> */}
        </div>
        <hr className="mb-3" />
        <ExportData />
        <hr className="mt-3 mb-4" />
        <UpgradeSubscription />
      </Menu>
    </Card>
  );
};

const MenuItemStyle = {
  backgroundColor: "#323a46",
  fontSize: 14,
  fontWeight: 500,
  color: "#fcf8e3",
};

export default LeftSideMenu;
