import React, { useEffect, useState } from "react";
import Chart from "react-apexcharts";
import { Card, Dropdown } from "react-bootstrap";
import { ApexOptions } from "apexcharts";
import { useSelector } from "react-redux";

const HeatChart = ({ loading }: { loading: any }) => {
  const hourlyCustomerCount = useSelector(
    (state: any) => state.Dashboard.hourlyCustomers
  );
  const customersForLastDays = useSelector(
    (state: any) => state.Dashboard.customersLastDays
  );
  const [selectedTimescale, setSelectedTimescale] = useState<string>("hourly");
  const [apexOpts, setApexOpts] = useState<ApexOptions>({
    chart: {
      type: "heatmap",
      toolbar: {
        show: false,
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
    plotOptions: {
      heatmap: {
        shadeIntensity: 0.5,
        colorScale: {
          ranges: [],
        },
      },
    },
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
      show: false,
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
    tooltip: {
      theme: "dark",
    },
  });

  const [apexData, setApexData] = useState<any>([
    {
      name: "Müşteri Yoğunluğu",
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

    setApexData([{ name: "Müşteri Yoğunluğu", data: customerCounts }]);

    setApexOpts((prevOpts) => ({
      ...prevOpts,
      plotOptions: {
        ...prevOpts.plotOptions,
        heatmap: {
          ...prevOpts?.plotOptions?.heatmap,
          colorScale: {
            ranges:
              selectedTimescale === "daily"
                ? [
                    { from: 0, to: 0, name: "low", color: "#ffffff" },
                    { from: 1, to: 50, name: "low", color: "#fffad0" },
                    { from: 51, to: 400, name: "low", color: "#ffff6d" },
                    { from: 401, to: 600, name: "medium", color: "#ffcb4d" },
                    { from: 601, to: 800, name: "high", color: "#ff8b4d" },
                    { from: 801, to: 3000, name: "extreme", color: "#FF254d" },
                  ]
                : [
                    { from: 0, to: 0, name: "low", color: "#ffffff" },

                    {
                      from: 1,
                      to: 10,
                      name: "low",
                      color: "#ffffff",
                    },
                    {
                      from: 11,
                      to: 20,
                      name: "medium",
                      color: "#fffad0",
                    },
                    {
                      from: 21,
                      to: 40,
                      name: "medium",
                      color: "#ffff6d",
                    },
                    {
                      from: 41,
                      to: 100,
                      name: "high",
                      color: "#ff8b4d",
                    },
                    {
                      from: 100,
                      to: 9999,
                      name: "extreme",
                      color: "#FF254d",
                    },
                  ],
          },
        },
      },
      xaxis: {
        ...prevOpts.xaxis,
        categories: timeLabels,
      },
    }));
  }, [hourlyCustomerCount, selectedTimescale, customersForLastDays]);

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
          Müşteri Yoğunluğu
        </h4>
        <div dir="ltr">
          <Chart
            options={apexOpts}
            series={apexData}
            type="heatmap"
            height={268}
            className="apex-charts mt-2"
          />
        </div>
      </Card.Body>
    </Card>
  );
};

export default HeatChart;
