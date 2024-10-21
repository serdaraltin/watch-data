import { Card, Dropdown } from "react-bootstrap";
import Chart from "react-apexcharts";
import { ApexOptions } from "apexcharts";

type StatisticsWidget1Props = {
  title: string;
  data: number;
  color: string;
  stats: number;
  subTitle: string;
  subStats: number;
};

const StatisticsWidget1 = ({
  title,
  data,
  color,
  stats,
  subTitle,
  subStats,
}: StatisticsWidget1Props) => {
  const apexOpts: ApexOptions = {
    chart: {
      type: "radialBar",
      sparkline: {
        enabled: true,
      },
    },
    dataLabels: {
      enabled: false,
    },
    plotOptions: {
      radialBar: {
        hollow: {
          margin: 0,
          size: "75%",
        },
        track: {
          background: color,
          opacity: 0.3,
          margin: 0,
        },
        dataLabels: {
          name: {
            show: false,
          },
          value: {
            show: true,
            color: color,
            fontWeight: 700,
            fontSize: "14px",
            offsetY: 5,
            formatter: (val: number) => {
              return String(val);
            },
          },
        },
      },
    },
    states: {
      hover: {
        filter: {
          type: "none",
        },
      },
    },
    colors: [color],
  };

  const apexData = [data];

  return (
    <Card>
      <Card.Body>
        {/* <Dropdown className="float-end" align="end">
          <Dropdown.Toggle as="a" className="cursor-pointer card-drop">
            <i className="mdi mdi-dots-vertical"></i>
          </Dropdown.Toggle>
          <Dropdown.Menu>
            <Dropdown.Item>Action</Dropdown.Item>
            <Dropdown.Item>Anothther Action</Dropdown.Item>
            <Dropdown.Item>Something Else</Dropdown.Item>
            <Dropdown.Item>Separated link</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown> */}
        <h5
          className="header-title"
          style={{ fontSize: 14, paddingBottom: 14, display: "flex" }}
        >
          {title}
        </h5>
        <div className="widget-chart-1" style={{ height: 48 }}>
          {/* <h2
            className="fw-normal"
            style={{ margin: 0, padding: 0, marginBottom: 10 }}
          >
            {stats}
          </h2> */}
          <div className="widget-chart-box-1 float-start">
            <Chart
              options={apexOpts}
              series={apexData}
              type="radialBar"
              width={85}
              height={85}
              className="apex-charts mt-0"
            />
          </div>
          <div
            className="widget-detail-1 text-end"
            style={{ margin: 0, padding: 0, paddingTop: 30, paddingBottom: 30 }}
          >
            <h3
              className="fw-normal pt-2 mb-1"
              style={{ fontSize: 24, margin: 0, padding: 0 }}
            >
              {subStats}
            </h3>
            <p
              className="text-muted mb-1"
              style={{ fontSize: 14, margin: 0, padding: 0 }}
            >
              {subTitle}
            </p>
          </div>
        </div>
      </Card.Body>
    </Card>
  );
};

export default StatisticsWidget1;
