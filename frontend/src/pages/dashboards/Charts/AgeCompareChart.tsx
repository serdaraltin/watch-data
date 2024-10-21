import { useEffect, useState } from "react";
import { ApexOptions } from "apexcharts";
import Chart from "react-apexcharts";
import { Card, Dropdown } from "react-bootstrap";
import config from "../../../config";
import { dayMockData } from "../../../data/mockData";

const workingHoursStart = config.workingHoursStart;
const workingHoursEnd = config.workingHoursEnd;

const AgeCompareChart: React.FC = () => {
  const [selectedTimescale, setSelectedTimescale] = useState<string>("Saatlik");
  const [options, setOptions] = useState<ApexOptions>({
    chart: {
      height: 350,
      type: "line",
      toolbar: {
        show: false,
      },
      stacked: false,
      zoom: {
        enabled: false,
      },
    },
    xaxis: {
      categories: [
        "8:00",
        "9:00",
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
        "19:00",
        "20:00",
        "21:00",
        "22:00",
        "23:00",
      ],
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: true,
      },
      labels: {
        style: {
          colors: "#4f5d75",
        },
      },
    },
    yaxis: {
      labels: {
        style: {
          colors: "#4f5d75",
        },
      },
    },
    grid: {
      show: false,
      padding: {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0,
      },
    },
    fill: {
      opacity: 1,
    },
    colors: ["#3bb9ff", "#ef476f", "#efa76f"],
    tooltip: {
      theme: "dark",
    },
  });

  const [series, setSeries] = useState([
    {
      name: "Genç Müşteri Sayısı",
      type: "line",
      data: [50, 75, 30, 50, 75, 50, 75, 100, 50, 75, 100, 75, 44, 66, 99, 111],
    },
    {
      name: "Yetişkin Müşteri Sayısı",
      type: "line",
      data: [50, 75, 12, 50, 15, 20, 35, 50, 80, 75, 90, 75, 100, 50, 75, 100],
    },
    {
      name: "Yaşlı Müşteri Sayısı",
      type: "line",
      data: [0, 40, 80, 40, 10, 40, 50, 70, 80, 40, 10, 40, 70, 80, 40, 10],
    },
  ]);

  const handleDropdownChange: (selectedOption: string | null) => void = (
    selectedOption: string | null
  ) => {
    if (selectedOption !== null) {
      setOptions((prevOptions) => ({
        ...prevOptions,
        xaxis: {
          categories:
            selectedOption === "monthly"
              ? [
                  "Ocak",
                  "Şubat",
                  "Mart",
                  "Nisan",
                  "Mayıs",
                  "Haziran",
                  "Temmuz",
                  "Ağustos",
                  "Eylül",
                  "Ekim",
                  "Kasım",
                  "Aralık",
                ]
              : selectedOption === "daily"
              ? ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]
              : selectedOption === "hourly"
              ? [
                  "10:00",
                  "11:00",
                  "12:00",
                  "13:00",
                  "14:00",
                  "15:00",
                  "16:00",
                  "17:00",
                  "18:00",
                  "19:00",
                  "20:00",
                  "21:00",
                ]
              : [],
        },
      }));
      selectedOption === "monthly" && setSelectedTimescale("Aylık");
      selectedOption === "daily" && setSelectedTimescale("Günlük");
      selectedOption === "hourly" && setSelectedTimescale("Saatlik");

      fetchData(selectedOption);
    }
  };

  // useEffect(() => {
  //   fetchData('hourly')
  //   fetchData('daily')
  //   fetchData('monthly')
  // }, [])

  // useEffect(() => {
  //   const intervalId = setInterval(() => {
  //     fetchData('hourly')
  //   }, 300000) //300000ms = 5 minutes

  //   //clear
  //   return () => {
  //     clearInterval(intervalId)
  //   }
  // }, [])

  const fetchData = async (selectedOption: string) => {
    let endpoint = config.BACKEND_URL;
    if (selectedOption === "hourly") {
      endpoint += "/hour";
    } else if (selectedOption === "daily") {
      endpoint += "/day";
    } else if (selectedOption === "monthly") {
      endpoint += "/month";
    }

    try {
      const storedData = localStorage.getItem(selectedOption);
      const storedTimestamp = localStorage.getItem(
        `${selectedOption}-timestamp`
      );
      const currentTimestamp = new Date().getTime();

      //less than 5 minutes old for hourly data don't fetch
      if (
        selectedOption === "hourly" &&
        storedData &&
        storedTimestamp &&
        currentTimestamp - parseInt(storedTimestamp, 10) < 300000
      ) {
        const data = JSON.parse(storedData);
        console.log("stored on local:", data);
        return;
      }

      //less than 60 minutes old for daily or monthly data don't fetch
      if (
        (selectedOption === "daily" || selectedOption === "monthly") &&
        storedData &&
        storedTimestamp &&
        currentTimestamp - parseInt(storedTimestamp, 10) < 3600000
      ) {
        const data = JSON.parse(storedData);
        console.log("stored on local:", data);
        return;
      }

      const response = await fetch(endpoint);
      if (!response.ok) {
        throw new Error(`http error! status: ${response.status}`);
      }

      let data = (await response.json()) ?? dayMockData.result;

      const workingHours = [];
      for (let i = workingHoursStart; i < workingHoursEnd; i++) {
        workingHours.push(i);
      }

      const filledData = workingHours.map((hour) => {
        const item = data.Obj.find((item: any) => item.timeLabel === hour);
        if (item) {
          return item;
        } else {
          return {
            startTime: hour,
            endTime: hour,
            timeLabel: hour,
            totalCustomers: 0,
            difference: 0,
            maleCustomers: { enter: 0, exit: 0 },
            femaleCustomers: { enter: 0, exit: 0 },
            isCompleted: true,
          };
        }
      });

      data.Obj = filledData;

      const maleData = data.Obj.map((item: any) => item.maleCustomers.enter);
      const femaleData = data.Obj.map(
        (item: any) => item.femaleCustomers.enter
      );

      setSeries([
        { name: "Kadın Müşteri Sayısı", type: "line", data: femaleData ?? [] },
        { name: "Erkek Müşteri Sayısı", type: "line", data: maleData ?? [] },
      ]);

      localStorage.setItem(selectedOption, JSON.stringify(data));
      localStorage.setItem(
        `${selectedOption}-timestamp`,
        currentTimestamp.toString()
      );

      console.log("fetched data:", data);
    } catch (error) {
      console.error("error fetch data:", error);
    }
  };

  return (
    <Card>
      <Card.Body>
        <Dropdown
          className="float-end"
          align="end"
          onSelect={handleDropdownChange}
        >
          <Dropdown.Toggle as="a" className="cursor-pointer card-drop">
            <i className="mdi mdi-dots-vertical"></i>
          </Dropdown.Toggle>
          <Dropdown.Menu>
            <Dropdown.Item eventKey="hourly">Saatlik</Dropdown.Item>
            <Dropdown.Item eventKey="daily">Günlük</Dropdown.Item>
            {/* <Dropdown.Item eventKey="monthly">Aylık</Dropdown.Item> */}
          </Dropdown.Menu>
        </Dropdown>

        <h4 className="header-title mt-0">
          {selectedTimescale} Yaş Karşılaştırması
        </h4>

        <div dir="ltr">
          <Chart
            options={options}
            series={series}
            type="line"
            height={268}
            className="apex-charts mt-2"
          />
        </div>
      </Card.Body>
    </Card>
  );
};

export default AgeCompareChart;
