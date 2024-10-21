import { Col, Row } from "react-bootstrap";
import { useEffect, useState } from "react";

// component
import BarChart from "./Charts/BarChart";
import CompareChart from "./Charts/CompareChart";
import HeatChart from "./Charts/HeatChart";
import DisabledCard from "../../components/DisabledCard";
import AgeCompareChart from "./Charts/AgeCompareChart";
import config from "../../config";
import { useDispatch, useSelector } from "react-redux";
import {
  setCustomersLastDays,
  setHourlyCustomers,
  setHourlyGender,
} from "../../redux/actions";
import {
  fetchDataForLastDays,
  fetchDataHourlyCount,
  fetchDataHourlyGender,
} from "../../utils/api/apis";

const ChartSection = () => {
  const dispatch = useDispatch();

  const selectedDate = useSelector(
    (state: any) => state.Dashboard.selectedDate
  );
  const selectedCamera = useSelector(
    (state: any) => state.Dashboard.selectedCamera
  );
  const refreshTime = useSelector((state: any) => state.Dashboard.refreshTime);

  const [loading, setLoading] = useState(false);

  const lastDaysRange = config.lastDaysRange;

  //calling fetch with interval and onmount
  useEffect(() => {
    const intervalId = setInterval(() => {
      // console.log(`fetching charts data ${refreshTime} ms period`);
      fetchDataHourlyCount(setLoading, selectedDate, selectedCamera).then(
        (data) => {
          dispatch(setHourlyCustomers(data));
        }
      );
      fetchDataHourlyGender(setLoading, selectedDate, selectedCamera).then(
        (data) => {
          dispatch(setHourlyGender(data));
        }
      );
      fetchDataForLastDays(
        selectedCamera,
        selectedDate,
        lastDaysRange,
        setLoading
      ).then((data) => {
        dispatch(setCustomersLastDays(data));
      });
    }, refreshTime);

    fetchDataHourlyCount(setLoading, selectedDate, selectedCamera).then(
      (data) => {
        dispatch(setHourlyCustomers(data));
      }
    );
    fetchDataHourlyGender(setLoading, selectedDate, selectedCamera).then(
      (data) => {
        dispatch(setHourlyGender(data));
      }
    );
    fetchDataForLastDays(
      selectedCamera,
      selectedDate,
      lastDaysRange,
      setLoading
    ).then((data) => {
      dispatch(setCustomersLastDays(data));
    });
    // clear
    return () => {
      clearInterval(intervalId);
    };
  }, [selectedCamera, refreshTime, selectedDate]);

  return (
    <>
      <Row>
        <Col xl={6}>
          <BarChart loading={loading} />
        </Col>
        <Col xl={6}>
          <CompareChart loading={loading} />
        </Col>
      </Row>
      <Row>
        <Col xl={6}>
          <HeatChart loading={loading} />
        </Col>
        <Col xl={6}>
          <DisabledCard cardHeight="md">
            <AgeCompareChart />
          </DisabledCard>
        </Col>
      </Row>
    </>
  );
};

export default ChartSection;
