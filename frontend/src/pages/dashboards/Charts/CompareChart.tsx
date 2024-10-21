import { useEffect, useState } from "react";
import { ApexOptions } from "apexcharts";
import Chart from "react-apexcharts";
import { Card, Dropdown } from "react-bootstrap";
import { useSelector } from "react-redux";

const CompareChart = ({ loading }: { loading: any }) => {
  const hourlyGenderCount = useSelector(
    (state: any) => state.Dashboard.hourlyGender
  );
  const customersForLastDays = useSelector(
    (state: any) => state.Dashboard.customersLastDays
  );
  const [selectedTimescale, setSelectedTimescale] = useState<string>("hourly");
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
    xaxis: {
      categories: [],
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
    colors: ["#3bb9ff", "#ef476f"],
    tooltip: {
      theme: "dark",
    },
  });

  const [series, setSeries] = useState([
    {
      name: "Kadın Müşteri Sayısı",
      type: "line",
      data: [],
    },
    {
      name: "Erkek Müşteri Sayısı",
      type: "line",
      data: [],
    },
  ]);

  const handleDropdownChange: (selectedOption: string | null) => void = (
    selectedOption: string | null
  ) => {
    if (selectedOption !== null) {
      selectedOption === "monthly" && setSelectedTimescale("Aylık");
      selectedOption === "daily" && setSelectedTimescale("daily");
      selectedOption === "hourly" && setSelectedTimescale("hourly");
    }
  };

  useEffect(() => {
    const timeLabels = hourlyGenderCount?.female?.map(
      (item: any) => item.time_label
    );
    const femaleCount = hourlyGenderCount?.female?.map(
      (item: any) => item.count
    );
    const maleCount = hourlyGenderCount?.male?.map((item: any) => item.count);
    setSeries([
      { name: "Erkek Müşteri Sayısı", type: "line", data: maleCount },
      { name: "Kadın Müşteri Sayısı", type: "line", data: femaleCount },
    ]);

    setOptions((prevOpts) => ({
      ...prevOpts,
      xaxis: {
        ...prevOpts.xaxis,
        categories: timeLabels,
      },
    }));
  }, [hourlyGenderCount]);
  useEffect(() => {
    const timeLabels =
      selectedTimescale === "hourly"
        ? hourlyGenderCount?.female?.map((item: any) => item.time_label)
        : selectedTimescale === "daily"
        ? customersForLastDays?.map((item: any) => item.time_label)
        : null;

    const femaleCount =
      selectedTimescale === "hourly"
        ? hourlyGenderCount?.female?.map((item: any) => item.count)
        : selectedTimescale === "daily"
        ? customersForLastDays?.map((item: any) => item.female)
        : null;

    const maleCount =
      selectedTimescale === "hourly"
        ? hourlyGenderCount?.male?.map((item: any) => item.count)
        : selectedTimescale === "daily"
        ? customersForLastDays?.map((item: any) => item.male)
        : null;

    setSeries([
      { name: "Erkek Müşteri Sayısı", type: "line", data: maleCount },
      { name: "Kadın Müşteri Sayısı", type: "line", data: femaleCount },
    ]);

    setOptions((prevOpts) => ({
      ...prevOpts,
      xaxis: {
        ...prevOpts.xaxis,
        categories: timeLabels,
      },
    }));
  }, [hourlyGenderCount, customersForLastDays, selectedTimescale]);

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
          Müşteri Kadın-Erkek Oranı
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

export default CompareChart;
