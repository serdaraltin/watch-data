import { Card, Dropdown } from "react-bootstrap";
import Chart from "react-apexcharts";
import { ApexOptions } from "apexcharts";
import { useState } from "react";

// const AgeTreeChart = ({ currentCustomers }: { currentCustomers: any }) => {
const AgeTreeChart = () => {
  const currentCustomers: { ages: { count: any }[] } = {
    ages: [{ count: 11 }, { count: 5 }, { count: 8 }],
  };
  const [apexOpts, setApexOpts] = useState<ApexOptions>({
    legend: {
      show: false,
    },
    chart: {
      height: 300,
      type: "treemap",
      toolbar: {
        show: false,
      },
    },
    dataLabels: {
      // enabled: true,
      // textAnchor: 'middle',
      style: {
        fontSize: "12px",
        colors: ["#ffffff"],
      },
      offsetY: -4,
    },

    // theme: {
    //   mode: 'light',
    //   palette: 'palette1',
    //   monochrome: {
    //     enabled: true,
    //     color: '#1E5D8C',
    //     shadeTo: 'light',
    //     shadeIntensity: 0.35,
    //   },
    // },
    colors: [
      "#ef476f",
      "#ffc43d",
      "#3bb9ff  ",
      "#06d6a0",
      "#EF6537",
      "#C1F666",
      "#f08080",
      "#0dcaf0",
      "#dc3545",
      "#421243",
      "#EF6537",
      "#F7B844",
      "#66cdaa",
      "#ff6347",
      "#ffd700",
      "#3B93A5",
      "#EC3C65",
      "#CDD7B6",
      "#C0ADDB",
      "#7F94B0",
    ],
    plotOptions: {
      treemap: {
        distributed: true,
        enableShades: false,
        useFillColorAsStroke: false,
      },
    },
    fill: {
      type: "solid",
      colors: ["red"],
    },
  });

  const apexData = [
    {
      data: [
        {
          x: "Genç",
          y:
            currentCustomers &&
            currentCustomers.ages &&
            currentCustomers.ages[0]
              ? currentCustomers.ages[0].count
              : 1,
        },
        {
          x: "Yetişkin",
          y:
            currentCustomers &&
            currentCustomers.ages &&
            currentCustomers.ages[1]
              ? currentCustomers.ages[1].count
              : 1,
        },
        {
          x: "Yaşlı",
          y:
            currentCustomers &&
            currentCustomers.ages &&
            currentCustomers.ages[2]
              ? currentCustomers.ages[2].count
              : 1,
        },
      ],
    },
  ];

  return (
    <Card>
      <Card.Body
        className="h-48"
        style={{
          display: "flex",
          justifyContent: "center",
          alignContent: "center",
          flexDirection: "column",
        }}
      >
        {/* <Dropdown
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
            <Dropdown.Item eventKey="monthly">Aylık</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown> */}
        <h4
          className="header-title mt-0"
          style={{
            marginLeft: 10,
          }}
        >
          Müşteri Yaş Dağılımı
        </h4>
        <div
          dir="ltr"
          style={{
            marginLeft: 10,
          }}
        >
          <Chart
            options={apexOpts}
            series={apexData}
            type="treemap"
            height={290}
            className="apex-charts "
          />
        </div>
      </Card.Body>
    </Card>
  );
};

export default AgeTreeChart;
