import { Button, Card, Container } from "react-bootstrap";
import { usePageTitle, useToggle } from "../../hooks";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import * as Yup from "yup";

import config from "../../config";
import { CameraItem, NewCameraItem } from "./types";
import NewCameraModal from "./NewCameraModal";
import UpdateCameraModal from "./UpdateCameraModal";
import CameraCardItem from "./CameraCardItem";
import { getAllCameras } from "../../utils/api/apis";

const validationSchema = Yup.object().shape({});

const CameraSetup = () => {
  usePageTitle({
    title: "Kamera Kurulumu",
    breadCrumbItems: [],
  });
  const [isAddCameraOpen, showAddCamera, hideAddCamera] = useToggle();
  const [isUpdateCameraOpen, showUpdateCamera, hideUpdateCamera] = useToggle();
  const [newCamera, setNewCamera] = useState<NewCameraItem>({
    branch_id: 1,
    resolution: "HD",
    install_date: "2024-01-23T12:00:00.000Z",
    status: true,
    type: "Digital",
    host: "",
    label: "Test Cam",
    model: "",
    protocol: "RTSP",
    user: "",
    password: "",
    channel: 1,
    port: 1,
    path: undefined,
    aditional: undefined,
  });
  const [cameras, setCameras] = useState<CameraItem[]>([]);

  const backendURL = config.BACKEND_URL;
  const serviceURL = config.SERVICE_URL;

  // const [cameras, setCameras] = useState<CameraItem[]>()
  const navigate = useNavigate();

  const handleInputChange = (event: any, index?: number) => {
    if (index && cameras) {
      const newCameras: any = [...cameras];
      newCameras[index][event.target.name] = event.target.value;
      setCameras(newCameras);
    } else {
      const { name, value } = event.target;
      setNewCamera((prevCamera) => ({
        ...prevCamera,
        [name]: value,
      }));
    }
  };

  const handleAddOperation = (camera: CameraItem) => {
    // const testObj = {
    //   label: 'New Camera',
    //   branch_id: 1,
    //   protocol: 'RTSP',
    //   host: '95.70.182.136',
    //   port: 554,
    //   user: 'itsumi',
    //   password: 'yu09ke17',
    //   channel: 3,
    //   resolution: 'HD',
    //   type: 'Digital',
    // }
    fetch(`${serviceURL}/api/camera/blur/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(camera),
      // body: JSON.stringify(testObj),
    })
      .then((response) => {
        console.log("res", response);
        return response.blob();
      })
      .then((blob) => {
        console.log("blob from blur>>>", blob);
        const newCameraImg = URL.createObjectURL(blob);
        console.log("newCameraImg from blur>>>", newCameraImg);
        newCameraImg &&
          navigate("/editor", {
            state: { cameras, newCamera, newCameraImg },
          });
      })
      .catch((error) => {
        console.log("Error", error.message);
        hideAddCamera();
        return;
      })
      .finally(() => {
        hideAddCamera();
      });
  };

  const handleEditPoints = (camera: CameraItem) => {
    fetch(`${serviceURL}/api/camera/blur/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(camera),
      // body: JSON.stringify(testObj),
    })
      .then((response) => {
        console.log("res", response);
        return response.blob();
      })
      .then((blob) => {
        console.log("blob from blur>>>", blob);
        const newCameraImg = URL.createObjectURL(blob);
        console.log("newCameraImg from blur>>>", newCameraImg);
        newCameraImg &&
          navigate("/editor", {
            state: { cameras, camera, newCameraImg },
          });
      })
      .catch((error) => {
        console.log("Error", error.message);
        hideAddCamera();
        return;
      })
      .finally(() => {
        hideAddCamera();
      });
  };

  const handleUpdateCamera = async (camera: CameraItem) => {
    try {
      const res = await fetch(`${backendURL}/api/v1/camera/:${camera.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(camera),
      });

      const data = await res.json();
      const updatedCamera = data.response;
      setCameras((prevCameras) =>
        prevCameras?.map((cam) => (cam.id === camera.id ? updatedCamera : cam))
      );
      console.log("updated from>>>", updatedCamera);
    } catch (error) {
      console.error("error on update cam:", error);
      return;
    }
    hideUpdateCamera();
  };

  const handleRemoveCamera = async (id: number) => {
    try {
      const response = await fetch(`${backendURL}/api/v1/camera/:${id}`, {
        method: "DELETE",
      });
      console.log("delete camera res>>>>", response);
      setCameras(cameras?.filter((camera) => camera.id !== id));
    } catch (error) {
      console.error("error on remove camera:", error);
    }
  };

  useEffect(() => {
    getAllCameras().then(setCameras);
  }, []);

  return (
    <>
      <Container style={{ height: "100%", paddingTop: 30, paddingBottom: 30 }}>
        <Card style={{ height: "100%", background: "#3a4250e5", padding: 20 }}>
          <h2 className="text-center m-3">Kamera Kurulumu</h2>
          {cameras?.map((camera, index) => (
            <Card className="p-0 position-relative" key={index}>
              <Card.Body>
                <CameraCardItem
                  handleRemoveCamera={handleRemoveCamera}
                  showUpdateCamera={showUpdateCamera}
                  handleEditPoints={handleEditPoints}
                  camera={camera}
                />
                <UpdateCameraModal
                  handleUpdateCamera={handleUpdateCamera}
                  isUpdateCameraOpen={isUpdateCameraOpen}
                  hideUpdateCamera={hideUpdateCamera}
                  handleInputChange={handleInputChange}
                  camera={camera}
                  index={index}
                />
              </Card.Body>
            </Card>
          ))}
          <div className="mt-2">
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                gap: 5,
              }}
            >
              <Button
                onClick={getAllCameras}
                style={{
                  width: "12rem",
                  maxWidth: "35vw",
                  borderRadius: 15,
                  fontWeight: 500,
                }}
                variant="warning"
              >
                Yenile
              </Button>
              <Button
                onClick={showAddCamera}
                variant="success"
                style={{
                  width: "12rem",
                  maxWidth: "35vw",
                  borderRadius: 15,
                  fontWeight: 500,
                }}
              >
                Kamera Ekle
              </Button>
            </div>
          </div>
        </Card>
        <NewCameraModal
          isAddCameraOpen={isAddCameraOpen}
          hideAddCamera={hideAddCamera}
          handleInputChange={handleInputChange}
          newCamera={newCamera}
          handleAddOperation={handleAddOperation}
        />
      </Container>
    </>
  );
};

export default CameraSetup;
