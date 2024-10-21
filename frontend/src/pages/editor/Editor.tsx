import React, { useEffect, useRef, useState } from "react";
import { Button, Card, Row } from "react-bootstrap";
import { useLocation } from "react-router-dom";
import { CameraItem } from "../camera-setup/types";

type Point = {
  x: number;
  y: number;
};

const EditorScreen: any = ({
  handleAddCamera,
  handleUpdateCamera,
}: {
  handleAddCamera: any;
  handleUpdateCamera: any;
}) => {
  const location = useLocation();
  const {
    newCamera,
    newCameraImg: camImage,
    camera,
  }: {
    newCamera: CameraItem;
    newCameraImg: string;
    camera: CameraItem;
  } = location.state;

  console.log("camImage", camImage);
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const [points, setPoints] = useState<any>(
    camera ? camera?.aditional?.points : []
  );
  const [dragPointIndex, setDragPointIndex] = useState<number | null>(null);
  const handleClear = () => {
    setPoints([]);
  };
  const handleComplete = () => {
    console.log("points saved. points:", points);

    let cameraModel = newCamera
      ? {
          branch_id: newCamera.branch_id,
          model: newCamera.model,
          user: newCamera.user,
          password: newCamera.password,
          resolution: newCamera.resolution,
          install_date: newCamera.install_date,
          type: newCamera.type,
          status: newCamera.status,
          protocol: newCamera.protocol,
          host: newCamera.host,
          port: newCamera.port,
          label: newCamera.label,
          channel: newCamera.channel,
          aditional: {},
        }
      : camera
      ? {
          branch_id: camera.branch_id,
          model: camera.model,
          user: camera.user,
          password: camera.password,
          resolution: camera.resolution,
          install_date: camera.install_date,
          type: camera.type,
          status: camera.status,
          protocol: camera.protocol,
          host: camera.host,
          port: camera.port,
          label: camera.label,
          channel: camera.channel,
          aditional: {},
        }
      : null;

    if (cameraModel && newCamera) {
      cameraModel.aditional = { points };
      handleAddCamera(cameraModel);
      console.log("camera saved to add>>>", cameraModel);
    } else if (cameraModel && camera) {
      cameraModel.aditional = { points };
      handleUpdateCamera(cameraModel);
      console.log("camera saved to update>>>", cameraModel);
    } else {
      console.log("no camera model to save");
    }
  };

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) {
      return;
    }

    const canvasWidth = canvas?.width;
    const canvasHeight = canvas?.height;

    const ctx = canvas.getContext("2d");
    if (!ctx) {
      return;
    }

    function handleMouseDown(event: MouseEvent) {
      const rect = canvas?.getBoundingClientRect();
      if (!rect) {
        return;
      }
      const x = (event.clientX - rect.left) / rect.width;
      const y = (event.clientY - rect.top) / rect.height;

      for (let i = 0; i < points.length; i++) {
        const point = points[i];
        const dx = x - point.x;
        const dy = y - point.y;
        if (Math.sqrt(dx * dx + dy * dy) < 5 / rect.width) {
          setDragPointIndex(i);
          return;
        }
      }

      setPoints((prevPoints: any) => {
        const newPoints = [...prevPoints, { x, y }];
        redraw(newPoints);
        return newPoints;
      });

      console.log(`point created (x:${x}, y:${y})`);
    }

    function handleMouseMove(event: MouseEvent) {
      if (dragPointIndex === null) {
        return;
      }
      const rect = canvas?.getBoundingClientRect();
      if (!rect) {
        return;
      }
      const x = (event.clientX - rect.left) / rect.width;
      const y = (event.clientY - rect.top) / rect.height;

      setPoints((prevPoints: any) => {
        const newPoints = [...prevPoints];
        newPoints[dragPointIndex] = { x, y };
        redraw(newPoints);
        return newPoints;
      });

      console.log(`point moved (x:${x}, y:${y})`);
    }

    function handleMouseUp() {
      setDragPointIndex(null);
    }

    function handleUndo() {
      setPoints((prevPoints: any) => {
        const newPoints = [...prevPoints];
        newPoints.pop();
        redraw(newPoints);
        console.log(`last point removed`);

        return newPoints;
      });
    }

    function redraw(points: Point[]) {
      if (ctx) {
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);
        points.forEach((point) =>
          drawPoint(point.x * canvasWidth, point.y * canvasHeight)
        );
        if (points.length > 1) {
          connectPoints(points);
        }
      }
    }

    function drawPoint(x: number, y: number) {
      if (ctx) {
        ctx.fillStyle = "cyan";
        ctx.beginPath();
        ctx.arc(x, y, 2, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    function connectPoints(points: Point[]) {
      if (ctx) {
        ctx.strokeStyle = "magenta";
        ctx.beginPath();
        ctx.moveTo(points[0].x * canvasWidth, points[0].y * canvasHeight);
        for (let i = 1; i < points.length; i++) {
          ctx.lineTo(points[i].x * canvasWidth, points[i].y * canvasHeight);
        }
        ctx.closePath();
        ctx.stroke();
      }
    }

    const handleKeyDown = (event: KeyboardEvent) => {
      // ctrl or cmd + Z check
      if ((event.ctrlKey || event.metaKey) && event.key === "z") {
        handleUndo();
      }

      // Enter check
      if (event.key === "Enter") {
        handleComplete();
      }
    };
    console.log("points>>", points);
    //keypress listener for keyboard
    window.addEventListener("keydown", handleKeyDown);

    canvas.addEventListener("mousedown", handleMouseDown);
    canvas.addEventListener("mousemove", handleMouseMove);
    canvas.addEventListener("mouseup", handleMouseUp);
    document.getElementById("undo")?.addEventListener("click", handleUndo);

    return () => {
      canvas.removeEventListener("mousedown", handleMouseDown);
      canvas.removeEventListener("mousemove", handleMouseMove);
      canvas.removeEventListener("mouseup", handleMouseUp);
      document.getElementById("undo")?.removeEventListener("click", handleUndo);
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, [points, dragPointIndex]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const img = new Image();
    img.src = camImage;
    img.onload = () => {
      canvas.width = img.naturalWidth;
      canvas.height = img.naturalHeight;
      ctx.drawImage(img, 0, 0, img.width, img.height);
    };
    console.log(
      "editore gönderildi. newCamera>>>>",
      newCamera,
      "camImage>>>>",
      camImage,
      "camera>>>>",
      camera
    );
  }, [camImage, newCamera, camera]);

  return (
    <Card
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "start",
        height: "calc(100% - 10rem)",
        boxSizing: "border-box",
        background: "#3a4250e5",
        marginTop: 20,
        padding: "1rem 2rem",
      }}
    >
      <canvas
        ref={canvasRef}
        style={{
          display: "block",
          backgroundColor: "transparent",
          border: "1px solid #4382bd",
          height: "100%",
          width: "100%",
          marginTop: 30,
          backgroundImage: `url(${camImage})`,
          backgroundPosition: "center",
          backgroundRepeat: "no-repeat",
          backgroundSize: "100%",
        }}
      />
      <Row
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "center",
          gap: 50,
          alignItems: "center",
          margin: "auto",
          width: "100%",
          marginTop: 20,
          marginBottom: 50,
        }}
      >
        <Button
          id="undo"
          variant="primary"
          style={{
            alignItems: "center",
            width: "8rem",
            textAlign: "center",
            borderRadius: 30,
          }}
        >
          Geri Al
        </Button>
        <Button
          onClick={handleClear}
          variant="primary"
          style={{
            alignItems: "center",
            width: "8rem",
            textAlign: "center",
            borderRadius: 30,
          }}
        >
          Temizle
        </Button>
        <Button
          onClick={handleComplete}
          variant="primary"
          style={{
            alignItems: "center",
            width: "8rem",
            textAlign: "center",
            borderRadius: 30,
          }}
        >
          Kaydet
        </Button>
      </Row>
    </Card>
  );
};

export default EditorScreen;
