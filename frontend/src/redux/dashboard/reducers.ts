import { setIsCurrentDataShowing } from "./actions";
import { DashboardAction, DashboardState } from "./constants";

const initialState: DashboardState = {
  selectedBranch: "all",
  refreshTime: 60000,
  // selectedCamera: 'all',
  //default for pera
  selectedCamera: "2",
  currentCustomers: [],
  customersLastDays: [],
  currentGender: [],
  hourlyGender: [],
  hourlyCustomers: [],
  companyBranches: [],
  companyInfo: [],
  branches: [],
  selectedDate: new Date(),
  isCurrentDataShowing: true,
};
const Dashboard = (
  state: DashboardState = initialState,
  action: {
    type: DashboardAction;
    payload: any;
  }
) => {
  switch (action.type) {
    case DashboardAction.SET_SELECTED_BRANCH:
      return {
        ...state,
        selectedBranch: action.payload,
      };
    case DashboardAction.SET_REFRESH_TIME:
      return {
        ...state,
        refreshTime: action.payload,
      };
    case DashboardAction.SET_SELECTED_CAMERA:
      return {
        ...state,
        selectedCamera: action.payload,
      };
    case DashboardAction.SET_CURRENT_CUSTOMERS:
      return {
        ...state,
        currentCustomers: action.payload,
      };
    case DashboardAction.SET_CUSTOMERS_LAST_DAYS:
      return {
        ...state,
        customersLastDays: action.payload,
      };
    case DashboardAction.SET_HOURLY_GENDER:
      return {
        ...state,
        hourlyGender: action.payload,
      };
    case DashboardAction.SET_CURRENT_GENDER:
      return {
        ...state,
        currentGender: action.payload,
      };
    case DashboardAction.SET_HOURLY_CUSTOMERS:
      return {
        ...state,
        hourlyCustomers: action.payload,
      };
    case DashboardAction.SET_COMPANY_BRANCHES:
      return {
        ...state,
        companyBranches: action.payload,
      };
    case DashboardAction.SET_BRANCHES:
      return {
        ...state,
        branches: action.payload,
      };
    case DashboardAction.SET_COMPANY_INFO:
      return {
        ...state,
        companyInfo: action.payload,
      };
    case DashboardAction.SET_SELECTED_DATE:
      return {
        ...state,
        selectedDate: action.payload,
      };
    case DashboardAction.SET_IS_CURRENTDATA_SHOWING:
      return {
        ...state,
        isCurrentDataShowing: action.payload,
      };
    default:
      return { ...state };
  }
};

export default Dashboard;
