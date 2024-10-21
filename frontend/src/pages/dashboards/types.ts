export type Message = {
  id: number;
  avatar: string;
  sender: string;
  text: string;
  time: string;
};

export type ProjectDetail = {
  id: number;
  name: string;
  startDate: string;
  dueDate: string;
  status: string;
  variant: string;
  clients: string;
};

export type currentCustomersItem = {
  count: number;
  female: number;
  male: number;
};

export type currentCustomersBody = {
  branch_id: number;
  camera_id?: number;
  between: {
    start_date: any;
    end_date: any;
  };
};

export type hourlyCustomersBody = {
  branch_id: number;
  camera_id?: number;
  day: any;
  working_hours: number[];
};

export type CameraCount = {
  label: string;
  count: number;
};
