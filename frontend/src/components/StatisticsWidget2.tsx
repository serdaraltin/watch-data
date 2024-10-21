import classNames from "classnames";
import { Badge, Card, Dropdown, ProgressBar } from "react-bootstrap";

type StatisticsWidgetProps = {
  variant: string;
  title: string;
  trendValue: string;
  trendIcon: string;
  stats: number;
  subTitle: string;
  progress: number;
  subStats: number;
};

const StatisticsWidget2 = ({
  variant,
  title,
  trendValue,
  trendIcon,
  stats,
  subTitle,
  subStats,
  progress,
}: StatisticsWidgetProps) => {
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
        <div className="widget-box-2" style={{ height: 120 }}>
          <h5 className="fw-normal" style={{ margin: 0, padding: 0 }}>
            {title}
          </h5>
          <h2
            className="fw-normal"
            style={{
              fontSize: 42,
              margin: 0,
              padding: 0,
              marginBottom: 10,
              marginTop: 5,
            }}
          >
            {stats}
          </h2>
          <div className="widget-detail-2 text-end ">
            {/* <Badge bg={variant} pill className="float-start ">
              {trendValue} <i className={trendIcon}></i>
            </Badge> */}
            <h3
              className="fw-normal"
              style={{ fontSize: 26, margin: 0, padding: 0, paddingBottom: 2 }}
            >
              {subStats}
            </h3>
            <p
              className="text-muted"
              style={{
                fontSize: 14,
                margin: 0,
                marginBottom: 0,
                padding: 0,
                paddingBottom: 5,
              }}
            >
              {subTitle}
            </p>
          </div>
          {/* <ProgressBar
            variant={variant}
            now={progress}
            className={classNames('progress-sm', 'progress-bar-alt-' + variant)}
          ></ProgressBar> */}
        </div>
      </Card.Body>
    </Card>
  );
};

export default StatisticsWidget2;
