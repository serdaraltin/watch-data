import { Button } from "react-bootstrap";

const UpgradeSubscription = () => {
  const openInNewTab = (url: string) => {
    const newWindow = window.open(url, "_blank", "noopener,noreferrer");
    if (newWindow) newWindow.opener = null;
  };
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          borderRadius: 30,
          border: "solid 2px #ffffff40",
          width: 180,
          padding: 15,
          paddingTop: 25,
          paddingBottom: 25,
          alignSelf: "center",
          textAlign: "center",
          marginTop: "auto",
        }}
      >
        <h5>Yeni Şube Ekle</h5>
        <p>Yeni şube eklemek için aşağıdaki linkten hesabınızı yükseltin.</p>
        <Button
          variant="primary"
          style={{
            fontSize: 14,
            borderRadius: 15,
            paddingTop: 10,
            paddingBottom: 10,
          }}
          onClick={() => openInNewTab("https://www.watchdata.ai/#pricing")}
        >
          + Hesabını Yükselt
        </Button>
      </div>
    </div>
  );
};

export default UpgradeSubscription;
