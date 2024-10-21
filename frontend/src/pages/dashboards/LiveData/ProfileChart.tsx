import { Card } from "react-bootstrap";
import Chart from "react-apexcharts";
import { ApexOptions } from "apexcharts";
import { useSelector } from "react-redux";

const ProfileChart = () => {
  const currentCustomers = useSelector(
    (state: any) => state.Dashboard.currentCustomers
  );
  const apexOpts: ApexOptions = {
    chart: {
      type: "donut",
    },
    noData: {
      text: "Veri Yok",
      align: "center",
      verticalAlign: "middle",
      style: {
        color: "#98a6ad",
        fontSize: "14px",
      },
    },
    // fill: {
    //   type: 'gradient',
    // },
    plotOptions: {
      pie: {
        expandOnClick: true,
        donut: {
          labels: {
            show: true,
            name: {
              show: true,
              formatter: (val: string) => {
                return val;
              },
              offsetY: 4,
              color: "#98a6ad",
            },
            value: {
              show: true,
              formatter: (val: string) => {
                return val;
              },
              color: "#98a6ad",
            },
          },
        },
      },
    },
    dataLabels: {
      enabled: false,
    },
    colors: ["#ef476f", "#3bb9ff"],
    legend: {
      show: true,
      position: "bottom",
      height: 40,
      labels: {
        useSeriesColors: true,
      },
    },
    labels: ["Kadın", "Erkek"],
    tooltip: {
      enabled: false,
    },
  };

  const apexData = [
    currentCustomers?.female > 0 ? currentCustomers?.female : 1,
    currentCustomers?.male > 0 ? currentCustomers?.male : 1,
  ];

  return (
    <Card>
      <Card.Body className="h-48">
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

        <h4 className="header-title mt-0">Cinsiyet Dağılımı (Bugün)</h4>

        <div dir="ltr">
          <Chart
            options={apexOpts}
            series={apexData}
            type="donut"
            height={322}
            className="apex-charts "
          />
        </div>
      </Card.Body>
    </Card>
  );
};

export default ProfileChart;
