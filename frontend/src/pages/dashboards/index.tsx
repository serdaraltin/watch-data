import { useState, useEffect } from "react";
import { Col, Row } from "react-bootstrap";

// hooks
import { usePageTitle } from "../../hooks";

// component
import LiveDataSection from "./LiveDataSection";
// import BranchTable from "./BranchTable";
import ChartSection from "./ChartsSection";
import LeftSideMenu from "./SideMenu";
import { useDispatch } from "react-redux";
import {
  setBranches,
  setCompanyBranches,
  setCompanyInfo,
} from "../../redux/actions";
import { getAllBranches, getCompanyInfo } from "../../utils/api/apis";

const DashBoard = () => {
  const dispatch = useDispatch();

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

  useEffect(() => {
    getCompanyInfo().then((data: any) => {
      dispatch(setCompanyInfo(data));
    });
    getAllBranches().then((data: any) => {
      dispatch(setCompanyBranches(data));
      dispatch(setBranches(data));
    });
  }, []);

  return (
    <div
      style={{
        display: "flex",
      }}
    >
      <LeftSideMenu />
      <div style={{ flex: 1 }}>
        <Row>
          <Col>
            <LiveDataSection />
          </Col>
        </Row>
        <Row>
          <Col xl={12}>
            <ChartSection />
          </Col>
        </Row>
        {/* <Row>
          <Col xl={12}>
            <BranchTable />
          </Col>
        </Row> */}
      </div>
    </div>
  );
};

export default DashBoard;
