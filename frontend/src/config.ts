import userImage from "../src/assets/wd-assets/user-images/minoa-logo.jpg";

const config = {
  API_URL: process.env.REACT_APP_API_URL,
  BACKEND_URL: process.env.BACKEND_URL || "https://backend.watchdata.ai",
  SERVICE_URL: process.env.SERVICE_URL || "https://dev.service.watchdata.ai",
  targetHourlyCustomers: 1200,
  workingHoursStart: 8,
  workingHoursEnd: 24,
  branchId: 2,
  entranceCam: 6,
  lastDaysRange: 7,
  companyId: 1,
  ignoreDateBefore: "2024-02-21",
  branchName: "Pera",
  userName: "Minoa",
  userLogo: userImage,
};

export default config;
