import {
  CameraCount,
  currentCustomersBody,
  hourlyCustomersBody,
} from "../../pages/dashboards/types";
import config from "../../config";
import { formatDate, formatDateForWeekLabel } from "../helpers";

//endpoints
let endpointCount = `${config.SERVICE_URL}/api/data/current_customer`;
let endpointGender = `${config.SERVICE_URL}/api/data/current_gender`;
let endpointHourlyGender = `${config.SERVICE_URL}/api/data/hourly_gender`;
let endpointHourlyCount = `${config.SERVICE_URL}/api/data/hourly_customer`;
const workingHours = [config.workingHoursStart, config.workingHoursEnd];

//config
const workingHoursEnd = config.workingHoursEnd;
const workingHoursStart = config.workingHoursStart;

export const fetchDataCurrentCustomers = async (
  start_date: any,
  end_date: any,
  selectedCamera: any
) => {
  let body: currentCustomersBody = {
    branch_id: config.branchId,
    between: {
      start_date: start_date,
      end_date: end_date,
    },
  };
  if (selectedCamera.includes("-")) {
    const [branchValue, cameraValue] = selectedCamera.split("-");
    body.branch_id = Number(branchValue);
    body.camera_id = Number(cameraValue);
  } else {
    body.branch_id = Number(selectedCamera);
    body.camera_id = config.entranceCam;
  }

  if (selectedCamera === "all") {
    body.branch_id = config.branchId;
    body.camera_id = config.entranceCam;
  }
  try {
    const response = await fetch(endpointCount, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
    if (!response.ok) {
      throw new Error(`http error! status: ${response.status}`);
    }
    const data = await response.json();
    return data.message.current_customer;
  } catch (error) {
    console.error("error fetch data currentcustomers :", error);
  }
};

export const fetchDataCurrentGender = async (
  start_date: any,
  end_date: any,
  selectedCamera: any
) => {
  let body: currentCustomersBody = {
    branch_id: config.branchId,
    between: {
      start_date: start_date,
      end_date: end_date,
    },
  };
  if (selectedCamera.includes("-")) {
    const [branchValue, cameraValue] = selectedCamera.split("-");
    body.branch_id = Number(branchValue);
    body.camera_id = Number(cameraValue);
  } else {
    body.branch_id = Number(selectedCamera);
    body.camera_id = config.entranceCam;
  }

  if (selectedCamera === "all") {
    body.branch_id = config.branchId;
    body.camera_id = config.entranceCam;
  }
  try {
    const response = await fetch(endpointGender, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
    if (!response.ok) {
      throw new Error(`http error! status: ${response.status}`);
    }
    const data = await response.json();
    return data.message;
  } catch (error) {
    console.error("error fetch data current_gender :", error);
  }
};

export const fetchDataHourlyCount = async (
  setLoading: (loading: boolean) => void,
  selectedDate: any,
  selectedCamera: any
) => {
  setLoading(true);

  let body: hourlyCustomersBody = {
    branch_id: config.branchId,
    day: new Date(selectedDate).toJSON().slice(0, 10),
    working_hours: workingHours,
  };
  if (selectedCamera.includes("-")) {
    const [branchValue, cameraValue] = selectedCamera.split("-");
    body.branch_id = Number(branchValue);
    body.camera_id = Number(cameraValue);
  } else {
    body.branch_id = Number(selectedCamera);
    body.camera_id = config.entranceCam;
    // body.camera_id = undefined;
    // endpointHourlyCount = `${config.SERVICE_URL}/api/data/hourly_customer/all`;
    // endpointHourlyGender = `${config.SERVICE_URL}/api/data/hourly_gender/all`;
  }

  //all branches
  if (selectedCamera === "all") {
    body.branch_id = config.branchId;
    body.camera_id = config.entranceCam;
    // body.camera_id = undefined;
  }
  try {
    const response = await fetch(endpointHourlyCount, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
    if (!response.ok) {
      throw new Error(`http error! status: ${response.status}`);
    }
    const data = await response?.json();
    setLoading(false);
    return data?.message?.hourly_customer;
  } catch (error) {
    console.error("error fetch data hourly_customer :", error);
    setLoading(false);
  }
};

export const fetchDataHourlyGender = async (
  setLoading: (loading: boolean) => void,
  selectedDate: any,
  selectedCamera: any
) => {
  setLoading(true);
  let body: hourlyCustomersBody = {
    branch_id: config.branchId,
    day: new Date(selectedDate).toJSON().slice(0, 10),
    working_hours: workingHours,
  };
  if (selectedCamera.includes("-")) {
    const [branchValue, cameraValue] = selectedCamera.split("-");
    body.branch_id = Number(branchValue);
    body.camera_id = Number(cameraValue);
  } else {
    body.branch_id = Number(selectedCamera);
    body.camera_id = config.entranceCam;
    // body.camera_id = undefined;
    // endpointHourlyCount = `${config.SERVICE_URL}/api/data/hourly_customer/all`;
    // endpointHourlyGender = `${config.SERVICE_URL}/api/data/hourly_gender/all`;
  }

  //all branches
  if (selectedCamera === "all") {
    body.branch_id = config.branchId;
    body.camera_id = config.entranceCam;
    // body.camera_id = undefined;
  }
  try {
    const response = await fetch(endpointHourlyGender, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
    if (!response.ok) {
      throw new Error(`http error! status: ${response.status}`);
    }
    const data = await response?.json();
    setLoading(false);
    return data?.message;
  } catch (error) {
    console.error("error fetch data hourly_gender :", error);
    setLoading(false);
  }
};

export const fetchDataForLastDays = async (
  selectedCamera: any,
  //   branch: any,
  selectedDate: Date,
  numDays: number,
  setLoading: any
) => {
  const ignoreDateBefore = new Date(config.ignoreDateBefore);
  setLoading(true);
  let responses = [];
  for (let i = 0; i < numDays; i++) {
    let date = new Date(selectedDate);
    date.setDate(date.getDate() - i);
    let start_date = formatDate(
      new Date(date.setHours(workingHoursStart, 0, 0, 0))
    );
    let end_date = formatDate(
      new Date(date.setHours(workingHoursEnd, 0, 0, 0))
    );

    let body: currentCustomersBody = {
      branch_id: config.branchId,
      between: {
        start_date: start_date,
        end_date: end_date,
      },
    };

    if (selectedCamera && selectedCamera?.includes("-")) {
      const [branchValue, cameraValue] = selectedCamera.split("-");
      body.branch_id = Number(branchValue);
      body.camera_id = Number(cameraValue);
    } else {
      body.branch_id = Number(selectedCamera);
      body.camera_id = config.entranceCam;
    }

    if (selectedCamera && selectedCamera === "all") {
      body.branch_id = config.branchId;
      body.camera_id = config.entranceCam;
    }

    try {
      const responseCount = fetch(endpointCount, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      const responseGender = fetch(endpointGender, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });

      const [resCount, resGender] = await Promise.all([
        responseCount,
        responseGender,
      ]);

      if (!resCount.ok || !resGender.ok) {
        throw new Error(
          `http error! status: ${resCount.status}, ${resGender.status}`
        );
      }
      if (date < ignoreDateBefore) {
        responses.unshift({
          count: 0,
          female: 0,
          male: 0,
          time_label: formatDateForWeekLabel(date),
        });
      } else {
        const dataCount = await resCount.json();
        const dataGender = await resGender.json();

        responses.unshift({
          count: dataCount.message.current_customer,
          female: dataGender.message.current_female,
          male: dataGender.message.current_male,
          time_label: formatDateForWeekLabel(date),
        });
      }
    } catch (error) {
      console.error("error fetch data weekly:", error);
    }
  }
  setLoading(false);
  // console.log("customers for last days", responses);
  return responses;
};

export const fetchDataForDateRange = async (
  selectedCamera: any,
  startDate: Date,
  endDate: Date
) => {
  let start_date = formatDate(
    new Date(startDate.setHours(config.workingHoursStart, 0, 0, 0))
  );
  let end_date = formatDate(
    new Date(endDate.setHours(config.workingHoursEnd, 0, 0, 0))
  );

  let body: currentCustomersBody = {
    branch_id: config.branchId,
    between: {
      start_date: start_date,
      end_date: end_date,
    },
  };

  if (selectedCamera && selectedCamera?.includes("-")) {
    const [branchValue, cameraValue] = selectedCamera.split("-");
    body.branch_id = Number(branchValue);
    body.camera_id = Number(cameraValue);
  } else {
    body.branch_id = Number(selectedCamera);
    body.camera_id = config.entranceCam;
  }

  if (selectedCamera && selectedCamera === "all") {
    body.branch_id = config.branchId;
    body.camera_id = config.entranceCam;
  }

  try {
    const responseCount = fetch(endpointCount, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    const responseGender = fetch(endpointGender, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const [resCount, resGender] = await Promise.all([
      responseCount,
      responseGender,
    ]);

    if (!resCount.ok || !resGender.ok) {
      throw new Error(
        `http error! status: ${resCount.status}, ${resGender.status}`
      );
    }

    const dataCount = await resCount.json();
    const dataGender = await resGender.json();

    return {
      count: dataCount.message.current_customer,
      female: dataGender.message.current_female,
      male: dataGender.message.current_male,
      time_label: formatDateForWeekLabel(startDate),
    };
  } catch (error) {
    console.error("error fetch data:", error);
  }
};

export const getAllCameras = async () => {
  let body = {
    branch_id: config.branchId,
  };
  const response = await fetch(`${config.SERVICE_URL}/api/camera/list`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const data = await response.json();

  return data.message.cameras;
};

export const getAllBranches = async () => {
  let body = {
    company_id: config.companyId,
  };

  const response = await fetch(
    `${config.SERVICE_URL}/api/company/branch/list`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    }
  );
  const data = await response.json();
  console.log("getAllBranches>>>>", data);

  return data.message.branch_list;
};

export const getCompanyInfo = async () => {
  let body = {
    company_id: config.companyId,
  };
  const response = await fetch(`${config.SERVICE_URL}/api/company/info`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const data = await response.json();
  console.log("getCompanyInfo>>>>", data);

  return data.message.branch_list;
};

export const getBranchInfo = async () => {
  let body = {
    branch_id: config.branchId,
  };
  const response = await fetch(`${config.SERVICE_URL}/api/branch/info`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const data = await response.json();
  console.log("getBranchInfo>>>>", data);

  return data.message.branch_list;
};

export const fetchCamsData = async (
  cameras: any[],
  start_date: any,
  end_date: any
) => {
  let responses: CameraCount[] = [];
  for (let camera of cameras) {
    // if (camera.label === ignoredCamLabel) {
    //   continue;
    // }
    let body = {
      branch_id: config.branchId,
      camera_id: camera.id,
      between: {
        start_date: start_date,
        end_date: end_date,
      },
    };

    try {
      const responseCount = await fetch(endpointCount, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });

      if (!responseCount.ok) {
        throw new Error(`http error! status: ${responseCount.status}`);
      }

      const dataCount = await responseCount.json();

      responses.push({
        label: camera.label,
        count: dataCount.message.current_customer,
      });
    } catch (error) {
      console.error("error fetch data currentcustomers :", error);
    }
  }

  return responses;
};
