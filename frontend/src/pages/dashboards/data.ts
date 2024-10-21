// types
import config from "../../config";
import { CameraItem } from "../camera-setup/types";
import { Message, ProjectDetail } from "./types";

// images
// import avatar1 from '../../../assets/images/users/user-1.jpg'
// import avatar2 from '../../../assets/images/users/user-2.jpg'
// import avatar3 from '../../../assets/images/users/user-3.jpg'
// import avatar4 from '../../../assets/images/users/user-4.jpg'
// import avatar5 from '../../../assets/images/users/user-5.jpg'

export const branches: { id: number; name: string; cameras: CameraItem[] }[] = [
  {
    id: config.branchId,
    name: config.branchName,
    // value: '2',
    cameras: [
      // { value: '6', name: 'Giriş Kamerası' },
      // { value: '2', name: 'Çıkış Kamerası' },
    ],
  },
  // {
  //   id: 2,
  //   name: 'Şube 2',
  //   value: '3',
  //   cameras: [
  //     { value: 'camera1', name: 'Giriş Kamerası' },
  //     { value: 'camera2', name: 'Çıkış Kamerası' },
  //   ],
  // },
];

export const responseDay = {
  success: true,
  error: false,
  Obj: [
    {
      startTime: "10:00:00",
      endTime: "10:55:00",
      timeLabel: "10:00",
      totalCustomers: 6,
      difference: 0,
      maleCustomers: { enter: 3, exit: 2 },
      femaleCustomers: { enter: 3, exit: 4 },
      isCompleted: true,
    },
    {
      startTime: "11:00:00",
      endTime: "11:55:00",
      timeLabel: "11:00",
      totalCustomers: 11,
      difference: -2,
      maleCustomers: { enter: 5, exit: 8 },
      femaleCustomers: { enter: 6, exit: 5 },
      isCompleted: true,
    },
    {
      startTime: "12:00:00",
      endTime: "12:55:00",
      timeLabel: "12:00",
      totalCustomers: 17,
      difference: -2,
      maleCustomers: { enter: 7, exit: 12 },
      femaleCustomers: { enter: 10, exit: 7 },
      isCompleted: true,
    },
    // {
    //   startTime: '13:00:00',
    //   endTime: '13:55:00',
    //   timeLabel: '13:00',
    //   totalCustomers: 22,
    //   difference: -4,
    //   maleCustomers: { enter: 8, exit: 16 },
    //   femaleCustomers: { enter: 14, exit: 10 },
    //   isCompleted: true,
    // },
    // {
    //   startTime: '14:00:00',
    //   endTime: '14:55:00',
    //   timeLabel: '14:00',
    //   totalCustomers: 27,
    //   difference: -6,
    //   maleCustomers: { enter: 12, exit: 19 },
    //   femaleCustomers: { enter: 15, exit: 14 },
    //   isCompleted: true,
    // },
    {
      startTime: "15:00:00",
      endTime: "15:55:00",
      timeLabel: "15:00",
      totalCustomers: 32,
      difference: -8,
      maleCustomers: { enter: 13, exit: 23 },
      femaleCustomers: { enter: 19, exit: 17 },
      isCompleted: true,
    },
    {
      startTime: "16:00:00",
      endTime: "16:55:00",
      timeLabel: "16:00",
      totalCustomers: 39,
      difference: -6,
      maleCustomers: { enter: 16, exit: 25 },
      femaleCustomers: { enter: 23, exit: 20 },
      isCompleted: true,
    },
    {
      startTime: "17:00:00",
      endTime: "17:55:00",
      timeLabel: "17:00",
      totalCustomers: 44,
      difference: -8,
      maleCustomers: { enter: 17, exit: 29 },
      femaleCustomers: { enter: 27, exit: 23 },
      isCompleted: true,
    },
    {
      startTime: "18:00:00",
      endTime: "18:55:00",
      timeLabel: "18:00",
      totalCustomers: 50,
      difference: -8,
      maleCustomers: { enter: 19, exit: 34 },
      femaleCustomers: { enter: 31, exit: 24 },
      isCompleted: true,
    },
    {
      startTime: "19:00:00",
      endTime: "19:55:00",
      timeLabel: "19:00",
      totalCustomers: 57,
      difference: -6,
      maleCustomers: { enter: 23, exit: 37 },
      femaleCustomers: { enter: 34, exit: 26 },
      isCompleted: true,
    },
    {
      startTime: "20:00:00",
      endTime: "20:55:00",
      timeLabel: "20:00",
      totalCustomers: 62,
      difference: -8,
      maleCustomers: { enter: 25, exit: 39 },
      femaleCustomers: { enter: 37, exit: 31 },
      isCompleted: true,
    },
    {
      startTime: "21:00:00",
      endTime: "21:55:00",
      timeLabel: "21:00",
      totalCustomers: 70,
      difference: -4,
      maleCustomers: { enter: 29, exit: 42 },
      femaleCustomers: { enter: 41, exit: 32 },
      isCompleted: true,
    },
  ],
  hourlyAverage: { enter: 5.833333333333333 },
};

const messages: Message[] = [
  // {
  //   id: 1,
  //   avatar: avatar1,
  //   sender: 'Chadengle',
  //   text: "Hey! there I'm available...",
  //   time: '13:40 PM',
  // },
  // {
  //   id: 2,
  //   avatar: avatar2,
  //   sender: 'Tomaslau',
  //   text: "I've finished it! See you so...",
  //   time: '13:34 PM',
  // },
  // {
  //   id: 3,
  //   avatar: avatar3,
  //   sender: 'Stillnotdavid',
  //   text: 'This theme is awesome!',
  //   time: '13:17 PM',
  // },
  // {
  //   id: 4,
  //   avatar: avatar4,
  //   sender: 'Kurafire',
  //   text: 'Nice to meet you',
  //   time: '12:20 PM',
  // },
  // {
  //   id: 5,
  //   avatar: avatar5,
  //   sender: 'Shahedk',
  //   text: "Hey! there I'm available...",
  //   time: '10:15 PM',
  // },
];

const projectDetails: ProjectDetail[] = [
  {
    id: 1,
    name: "Tüm Şubeler",
    startDate: "01/01/2017",
    dueDate: "26/04/2017",
    status: "Released",
    variant: "danger",
    clients: "Coderthemes",
  },
  {
    id: 2,
    name: "Kelebek Vadi İstanbul Şubesi",
    startDate: "01/01/2017",
    dueDate: "26/04/2017",
    status: "Released",
    variant: "danger",
    clients: "Coderthemes",
  },

  // {
  //     id: 3,
  //     name: 'Adminto Admin v1.1',
  //     startDate: '01/05/2017',
  //     dueDate: '10/05/2017',
  //     status: 'Pending',
  //     variant: 'pink',
  //     clients: 'Coderthemes',
  // },
  // {
  //     id: 4,
  //     name: 'Adminto Frontend v1.1',
  //     startDate: '01/01/2017',
  //     dueDate: '31/05/2017',
  //     status: 'Work in Progress',
  //     variant: 'purple',
  //     clients: 'Adminto admin',
  // },
  // {
  //     id: 5,
  //     name: 'Adminto Admin v1.3',
  //     startDate: '01/01/2017',
  //     dueDate: '31/05/2017',
  //     status: 'Coming soon',
  //     variant: 'warning',
  //     clients: 'Coderthemes',
  // },
  // {
  //     id: 6,
  //     name: 'Adminto Admin v1.3',
  //     startDate: '01/01/2017',
  //     dueDate: '31/05/2017',
  //     status: 'Coming soon',
  //     variant: 'blue',
  //     clients: 'Adminto admin',
  // },
];

export { messages, projectDetails };
