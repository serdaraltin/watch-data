import { DashboardAction } from "./constants";

export const setSelectedBranch = (branch: string) => ({
  type: DashboardAction.SET_SELECTED_BRANCH,
  payload: branch,
});
export const setSelectedCamera = (camera: string) => ({
  type: DashboardAction.SET_SELECTED_CAMERA,
  payload: camera,
});

export const setRefreshTime = (time: number) => ({
  type: DashboardAction.SET_REFRESH_TIME,
  payload: time,
});

export const setCurrentCustomers = (data: any) => ({
  type: DashboardAction.SET_CURRENT_CUSTOMERS,
  payload: data,
});

export const setCustomersLastDays = (data: any) => ({
  type: DashboardAction.SET_CUSTOMERS_LAST_DAYS,
  payload: data,
});

export const setCurrentGender = (data: any) => ({
  type: DashboardAction.SET_CURRENT_GENDER,
  payload: data,
});
export const setHourlyCustomers = (data: any) => ({
  type: DashboardAction.SET_HOURLY_CUSTOMERS,
  payload: data,
});
export const setHourlyGender = (data: any) => ({
  type: DashboardAction.SET_HOURLY_GENDER,
  payload: data,
});
export const setBranches = (data: any) => ({
  type: DashboardAction.SET_BRANCHES,
  payload: data,
});
export const setCompanyBranches = (data: any) => ({
  type: DashboardAction.SET_COMPANY_BRANCHES,
  payload: data,
});
export const setCompanyInfo = (data: any) => ({
  type: DashboardAction.SET_COMPANY_INFO,
  payload: data,
});

export const setSelectedDate = (date: any) => ({
  type: DashboardAction.SET_SELECTED_DATE,
  payload: date,
});
export const setIsCurrentDataShowing = (date: any) => ({
  type: DashboardAction.SET_IS_CURRENTDATA_SHOWING,
  payload: date,
});
