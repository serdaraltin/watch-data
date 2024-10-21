import { setSelectedDate } from "./actions";
export enum DashboardAction {
  SET_SELECTED_BRANCH = "@@dashboard/SET_SELECTED_BRANCH",
  SET_REFRESH_TIME = "@@dashboard/SET_REFRESH_TIME",
  SET_SELECTED_CAMERA = "@@dashboard/SET_SELECTED_CAMERA",
  SET_CURRENT_CUSTOMERS = "@@dashboard/SET_CURRENT_CUSTOMERS",
  SET_CURRENT_GENDER = "@@dashboard/SET_CURRENT_GENDER",
  SET_HOURLY_CUSTOMERS = "@@dashboard/SET_HOURLY_CUSTOMERS",
  SET_HOURLY_GENDER = "@@dashboard/SET_HOURLY_GENDER",
  SET_CUSTOMERS_LAST_DAYS = "@@dashboard/SET_CUSTOMERS_LAST_DAYS",
  SET_BRANCHES = "@@dashboard/SET_BRANCHES",
  SET_COMPANY_BRANCHES = "@@dashboard/SET_COMPANY_BRANCHES",
  SET_COMPANY_INFO = "@@dashboard/SET_COMPANY_INFO",
  SET_SELECTED_DATE = "@@dashboard/SET_SELECTED_DATE",
  SET_IS_CURRENTDATA_SHOWING = "@@dashboard/SET_IS_CURRENTDATA_SHOWING",
}

export type DashboardState = {
  selectedCamera: string;
  selectedBranch: string;
  refreshTime: number;
  currentCustomers: any;
  currentGender: any;
  hourlyGender: any;
  hourlyCustomers: any;
  customersLastDays: any;
  companyBranches: any;
  companyInfo: any;
  branches: any;
  selectedDate: any;
  isCurrentDataShowing: boolean;
};
