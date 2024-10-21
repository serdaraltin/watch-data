import { Col, Row } from "react-bootstrap";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

// hooks
import { usePageTitle } from "../../hooks";
import { formatDate } from "../../utils/helpers";

import config from "../../config";

// component
import ProfileChart from "./LiveData/ProfileChart";
import AgeTreeChart from "./LiveData/AgeTreeChart";
import CurrentCustomersWidget from "./LiveData/CurrentCustomerWidget";
import TargetCustomersWidget from "./LiveData/TargetCustomerWidget";
import CameraComparison from "./LiveData/CameraComparison";
import GenderComparisonWidget from "./LiveData/GenderComparisonWidget";
import DisabledCard from "../../components/DisabledCard";
import { setCurrentCustomers } from "../../redux/dashboard/actions";
import {
  fetchDataCurrentCustomers,
  fetchDataCurrentGender,
  fetchDataForDateRange,
} from "../../utils/api/apis";

const LiveDataSection = () => {
  const dispatch = useDispatch();

  const selectedCamera = useSelector(
    (state: any) => state.Dashboard.selectedCamera
  );
  const isCurrentDataShowing = useSelector(
    (state: any) => state.Dashboard.isCurrentDataShowing
  );
  const selectedDate = useSelector(
    (state: any) => state.Dashboard.selectedDate
  );
  const refreshTime = useSelector((state: any) => state.Dashboard.refreshTime);
  // const [loading, setLoading] = useState(true)

  const [yesterdayTotalCustomers, setYesterdayTotalCustomers] = useState(null);

  // set pagetitle
  usePageTitle({
    title: "DashBoard",
    breadCrumbItems: [
      {
        path: "/dashboard",
        label: "DashBoard",
        active: true,
      },
    ],
  });

  //for requests
  let startDate = new Date(selectedDate);
  startDate.setHours(config.workingHoursStart, 0, 0, 0);
  let start_date = formatDate(startDate);
  // console.log("start_date>>>>>>>>>>>>>>>>>>>>>>>>>", start_date);
  const yesterday = new Date(selectedDate);
  yesterday.setDate(yesterday.getDate() - 1);

  let endDate = new Date(selectedDate);
  endDate.setHours(config.workingHoursEnd, 0, 0, 0);
  let end_date = formatDate(endDate);
  // console.log("end_date>>>>>>>>>>>>>>>>>>>>>>>>>", end_date);

  useEffect(() => {
    const intervalId = setInterval(() => {
      fetchData();
    }, refreshTime);

    const fetchData = async () => {
      const dataCount = await fetchDataCurrentCustomers(
        start_date,
        end_date,
        selectedCamera
      );
      const dataGender = await fetchDataCurrentGender(
        start_date,
        end_date,
        selectedCamera
      );

      dispatch(
        setCurrentCustomers({
          count: dataCount,
          female: dataGender.current_female,
          male: dataGender.current_male,
        })
      );
    };

    fetchData();

    fetchDataForDateRange(selectedCamera, yesterday, yesterday)
      .then((fetchedData: any) => {
        setYesterdayTotalCustomers(fetchedData);
      })
      .catch((error: any) => {
        console.error("Error fetching data:", error);
      });

    return () => {
      clearInterval(intervalId);
    };
  }, [selectedCamera, refreshTime, selectedDate]);

  return (
    <>
      <div>
        <Row>
          <Col
            xs={12}
            style={{
              display: "flex",
              flexDirection: "row-reverse",
              alignItems: "center",
              padding: "0.5rem 0.2rem 0.8rem 0",
            }}
          >
            <Col
              xs={12}
              md={8}
              style={{
                display: "flex",
                flexDirection: "row-reverse",
                alignItems: "center",
              }}
            ></Col>
          </Col>
        </Row>
        {isCurrentDataShowing && (
          <>
            <Row>
              <Col xl={4}>
                <CurrentCustomersWidget
                  yesterdayTotalCustomers={yesterdayTotalCustomers}
                />
              </Col>
              <Col xl={4}>
                <GenderComparisonWidget />
              </Col>
              <Col xl={4}>
                <TargetCustomersWidget />
              </Col>
            </Row>
            <Row>
              <Col xl={4}>
                <ProfileChart />
              </Col>
              <Col xl={4}>
                <CameraComparison />
              </Col>
              <Col xl={4}>
                <DisabledCard cardHeight="lg">
                  <AgeTreeChart />
                  {/* <AgeTreeChart currentCustomers={currentCustomers} /> */}
                </DisabledCard>
              </Col>
            </Row>
          </>
        )}
      </div>
    </>
  );
};

export default LiveDataSection;
