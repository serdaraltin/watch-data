import { useEffect, useState } from "react";
import { usePageTitle } from "../../hooks";
import CamerasTable from "./CamerasTable/CamerasTable";
import { useNavigate } from "react-router-dom";
import { CameraItem } from "../camera-setup/types";
import { getAllCameras } from "../../utils/api/apis";

const Cameras = () => {
  const [cameras, setCameras] = useState<CameraItem[]>([]);

  const navigate = useNavigate();

  usePageTitle({
    title: "Cameras",
    breadCrumbItems: [
      {
        path: "/cameras",
        label: "Cameras",
        active: true,
      },
    ],
  });

  const handleCams = () => {
    navigate("/camera-setup", { state: { cameras } });
  };

  useEffect(() => {
    getAllCameras().then(setCameras);
  }, []);

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <CamerasTable cameras={cameras} handleCams={handleCams} />
    </div>
  );
};

export default Cameras;
