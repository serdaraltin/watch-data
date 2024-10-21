import { useEffect, useState } from "react";
import { ApexOptions } from "apexcharts";
import Chart from "react-apexcharts";
import { Card, Dropdown } from "react-bootstrap";
import { useSelector } from "react-redux";
// import { useFilledData } from '../../../hooks'
// import { dayMockData } from '../../../data/mockData'

const BarChart = ({ loading }: { loading: any }) => {
  const [selectedTimescale, setSelectedTimescale] = useState<string>("hourly");
  // const [timeLabels, setTimeLabels] = useState<string[]>([])
  const hourlyCustomerCount = useSelector(
    (state: any) => state.Dashboard.hourlyCustomers
  );
  const customersForLastDays = useSelector(
    (state: any) => state.Dashboard.customersLastDays
  );

  const [apexOpts, setApexOpts] = useState<ApexOptions>({
    chart: {
      type: "bar",
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        columnWidth: "20%",
      },
    },
    // noData: {
    //   text: loading ? "Yükleniyor..." : "Veri Yok",
    //   align: "center",
    //   verticalAlign: "middle",
    //   offsetX: 0,
    //   offsetY: 0,
    //   style: {
    //     color: "#ffff",
    //     fontSize: "14px",
    //     fontFamily: "Helvetica",
    //   },
    // },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      show: false,
    },
    xaxis: {
      categories: [],
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
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
    colors: ["#3bb9ff"],
    tooltip: {
      theme: "dark",
    },
  });

  const [apexData, setApexData] = useState<any>([
    {
      name: "Müşteri Sayısı",
      data: [],
    },
  ]);

  const handleDropdownChange: (selectedOption: string | null) => void = (
    selectedOption: string | null
  ) => {
    if (selectedOption !== null) {
      selectedOption === "monthly" && setSelectedTimescale("monthly");
      selectedOption === "daily" && setSelectedTimescale("daily");
      selectedOption === "hourly" && setSelectedTimescale("hourly");
    }
  };

  useEffect(() => {
    const arr =
      selectedTimescale === "hourly"
        ? hourlyCustomerCount
        : selectedTimescale === "daily"
        ? customersForLastDays
        : null;
    const timeLabels = arr?.map((item: any) => item.time_label);
    const customerCounts = arr?.map((item: any) => item.count);
    setApexData([{ name: "Müşteri Sayısı", data: customerCounts }]);

    setApexOpts((prevOpts) => ({
      ...prevOpts,
      xaxis: {
        ...prevOpts.xaxis,
        categories: timeLabels,
      },
    }));
  }, [hourlyCustomerCount, customersForLastDays, selectedTimescale]);

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
          {selectedTimescale === "hourly"
            ? "Saatlik"
            : selectedTimescale === "daily"
            ? "Günlük"
            : ""}{" "}
          Müşteri Dağılımı
        </h4>

        <div dir="ltr">
          <Chart
            options={apexOpts}
            series={apexData}
            type="bar"
            height={268}
            className="apex-charts mt-2"
          />
        </div>
      </Card.Body>
    </Card>
  );
};

export default BarChart;
