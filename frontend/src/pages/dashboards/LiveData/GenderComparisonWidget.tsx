import { Card, Col, Row } from "react-bootstrap";

// component

import { useSelector } from "react-redux";

const GenderComparisonWidget = () => {
  const currentCustomers = useSelector(
    (state: any) => state.Dashboard.currentCustomers
  );
  return (
    <>
      <Card className="shadow-sm">
        <Card.Body
          className="d-flex flex-column  justify-content-center "
          style={{ height: 170, padding: 20 }}
        >
          <div className="w-100 pe-2 mb-3 d-flex flex-row align-items-center justify-content-between">
            <div className="w-100  d-flex flex-row align-items-center">
              <i
                className={"mdi mdi-circle  me-2"}
                style={{ color: "#ef476f" }}
              ></i>

              <h5 className=" mb-0  p-0 m-0 me-3" style={{ fontWeight: 500 }}>
                Bugünkü Kadın Müşteri:
              </h5>
            </div>
            <div className=" d-flex flex-row align-items-center w-50">
              {/* --------- */}
            </div>
            <h5
              className="mb-0 m-0 p-0  "
              style={{ fontSize: 26, color: "#ef476f" }}
            >
              {currentCustomers?.female
                ? // currentCustomers?.fecurrent_female?.total > 0
                  currentCustomers?.female
                : 0}
            </h5>
          </div>
          <div className="w-100 pe-2 d-flex flex-row align-items-center justify-content-between">
            <div className="w-100  d-flex flex-row align-items-center ">
              <i
                className={"mdi mdi-circle  me-2"}
                style={{ color: "#3bb9ff" }}
              ></i>

              <h5 className=" mb-0 p-0 m-0 me-3" style={{ fontWeight: 500 }}>
                Bugünkü Erkek Müşteri:
              </h5>
            </div>
            <div className="  d-flex flex-row align-items-center w-50">
              {/* --------- */}
            </div>
            <h5
              className="mb-0 m-0 p-0  "
              style={{ fontSize: 26, color: "#3bb9ff" }}
            >
              {currentCustomers?.male
                ? //currentCustomers?.current_male?.total > 0
                  currentCustomers?.male
                : 0}
            </h5>
          </div>
        </Card.Body>
      </Card>
    </>
  );
};

export default GenderComparisonWidget;

{
  /* <div className="user float-start me-3">
                                        <i className={classNames('mdi mdi-circle', 'text-' + reminder.variant)}></i>
                                    </div>
                                    <div className="user-desc overflow-hidden">
                                        <h5 className="name mt-0 mb-1">{reminder.title}</h5>
                                        <span className="desc text-muted font-12 text-truncate d-block">
                                            {reminder.date} - {reminder.time}
                                        </span>
                                    </div> */
}
