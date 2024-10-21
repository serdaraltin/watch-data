import React, { useEffect, useState } from "react";
import {
  InputGroup,
  FormControl,
  ToggleButton,
  Spinner,
} from "react-bootstrap";
import { Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import { useDispatch, useSelector } from "react-redux";
import { setSelectedCamera as setCameraSelection } from "../../../redux/actions";
import { branches } from "../data";
import config from "../../../config";
import { CameraItem } from "../../camera-setup/types";

let updatedBranches = [...branches];
const serviceURL = config.SERVICE_URL;
let branchId: number = config.branchId;

const BranchSearch = () => {
  const [searchTerm, setSearchTerm] = useState<string>("");
  const [cameras, setCameras] = useState<CameraItem[]>([]);
  const [isLoading, setIsLoading] = useState<any>({});
  const [openBranch, setOpenBranch] = useState<any>(null);

  const dispatch = useDispatch();

  const handleSearchChange = (event: any) => {
    setSearchTerm(event.target.value);
  };

  const selectedCamera = useSelector(
    (state: any) => state.Dashboard.selectedCamera
  );

  const handleCameraChange = (camera: string) => {
    dispatch(setCameraSelection(camera));
  };

  const handleBranchClick = async (branchId: number) => {
    if (openBranch === branchId) {
      setOpenBranch(null);
    } else {
      setIsLoading((prevState: any) => ({
        ...prevState,
        [branchId]: true,
      }));
      setOpenBranch(branchId);
      await getAllCameras(branchId);
      setIsLoading((prevState: any) => ({
        ...prevState,
        [branchId]: false,
      }));
    }
  };

  const getAllCameras = async (branchId: number) => {
    try {
      let body = {
        branch_id: branchId,
      };
      const response = await fetch(`${serviceURL}/api/camera/list`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      const data = await response.json();

      setCameras(data.message.cameras);
    } catch (error) {
      console.error("sidemenu get all cameras error:", error);
    }
  };

  // useEffect(() => {
  //   console.log("camera changed at store>>>>", selectedCamera);
  //   //branchId buradan setlenebilir
  // }, [selectedCamera]);

  useEffect(() => {
    updatedBranches[0].cameras = [...cameras];
  }, [cameras]);
  useEffect(() => {
    getAllCameras(branchId);
  }, [branchId]);

  return (
    <div className="mb-3 pb-3">
      <InputGroup className="p-2 pb-0 pt-1 mb-2">
        <FormControl
          placeholder="Şube Ara..."
          aria-label="Şube Ara..."
          onChange={handleSearchChange}
          style={{
            borderRadius: 15,
            color: "white",
            marginRight: 5,
            marginLeft: 5,
          }}
        />
      </InputGroup>
      <ToggleButton
        variant="darken"
        style={{
          textAlign: "start",
          paddingLeft: 20,
          border: 0,
          margin: 1,
          width: "99%",
          fontSize: 15,
          fontWeight: 500,
          marginBottom: 10,
          backgroundColor: selectedCamera === "all" ? "#4382bd" : "",
        }}
        value={"all"}
        checked={selectedCamera === "all" ? true : false}
        onClick={() => handleCameraChange("all")}
      >
        Tüm Şubeler
      </ToggleButton>
      <Menu
        style={{
          maxHeight: 250,
          overflowY: "auto",
          borderTop: "1px #ffffff10 solid",
          borderBottom: "1px #ffffff10 solid",
        }}
      >
        {updatedBranches
          ?.filter((branch) =>
            branch?.name.toLowerCase().includes(searchTerm.toLowerCase())
          )
          .map((branch, i) => (
            <SubMenu
              key={i}
              label={branch?.name}
              className="d-lg-block"
              style={{
                backgroundColor:
                  selectedCamera === branch?.id?.toString()
                    ? "#4382bd"
                    : "#323a46",
                textAlign: "start",
                paddingLeft: 20,
                border: 0,
                width: "99%",
                color: "#fcf8e3",
              }}
              defaultOpen={openBranch === branch?.id}
              // defaultOpen={!isLoading && selectedCamera === branch?.id?.toString()&& branch.cameras.length>0 ? true : false}
              onClick={() => {
                handleCameraChange(branch?.id?.toString());
                handleBranchClick(branch.id);
              }}
            >
              {isLoading[branch?.id] ? (
                <div
                  style={{
                    textAlign: "center",
                    backgroundColor: "#323a46",
                    color: "#fcf8e3",
                    height: 300,
                    margin: 0,
                    padding: 30,
                    marginTop: "-10px",
                  }}
                >
                  <h5>Yükleniyor...</h5>

                  <Spinner animation={"border"}></Spinner>
                </div>
              ) : (
                branch?.cameras?.map((camera, j) => (
                  <MenuItem
                    key={j}
                    icon={""}
                    style={{
                      backgroundColor:
                        selectedCamera ===
                        branch?.id?.toString() + "-" + camera?.id
                          ? "#4382bd"
                          : "#323a46",
                      fontSize: 14,
                      fontWeight: 500,
                      color: "#fcf8e3",
                    }}
                    onClick={() =>
                      handleCameraChange(
                        branch?.id?.toString() + "-" + camera?.id
                      )
                    }
                  >
                    {camera?.label}
                  </MenuItem>
                ))
              )}
            </SubMenu>
          ))}
      </Menu>
    </div>
  );
};

export default BranchSearch;
