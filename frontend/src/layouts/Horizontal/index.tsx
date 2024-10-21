import React, { Suspense, useEffect, useState } from "react";
import { Breadcrumb, Col, Container, FormCheck, Row } from "react-bootstrap";
import { Outlet } from "react-router-dom";

// actions
import { changeTopbarTheme } from "../../redux/actions";

// constants
import { LayoutTypes, TopbarTheme } from "../../constants/layout";
import bgImage from "../../assets/wd-assets/wdbg_2.png";

// hooks
import { useRedux } from "../../hooks";

// utils
import { changeBodyAttribute } from "../../utils";

// code splitting and lazy loading
// https://blog.logrocket.com/lazy-loading-components-in-react-16-6-6cea535c0b52
const Topbar = React.lazy(() => import("../Topbar"));
const Navbar = React.lazy(() => import("./Navbar"));
const Footer = React.lazy(() => import("../Footer"));

const loading = () => <div className="text-center"></div>;

type HorizontalLayoutProps = {
  children?: any;
};

const HorizontalLayout = ({ children }: HorizontalLayoutProps) => {
  const { dispatch, appSelector } = useRedux();

  const [isMenuOpened, setIsMenuOpened] = useState<boolean>(false);

  const {
    layoutColor,
    layoutWidth,
    menuPosition,
    topbarTheme,
    isOpenRightSideBar,
    pageTitle,
  } = appSelector((state) => ({
    layoutColor: state.Layout.layoutColor,
    layoutWidth: state.Layout.layoutWidth,
    menuPosition: state.Layout.menuPosition,
    topbarTheme: state.Layout.topbarTheme,
    isOpenRightSideBar: state.Layout.isOpenRightSideBar,
    pageTitle: state.PageTitle.pageTitle,
  }));

  /*
    layout defaults
    */
  useEffect(() => {
    changeBodyAttribute("data-layout-mode", LayoutTypes.LAYOUT_HORIZONTAL);
    dispatch(changeTopbarTheme(TopbarTheme.TOPBAR_THEME_DARK));
  }, [dispatch]);

  useEffect(() => {
    changeBodyAttribute("data-layout-color", layoutColor);
  }, [layoutColor]);

  useEffect(() => {
    changeBodyAttribute("data-layout-size", layoutWidth);
  }, [layoutWidth]);

  useEffect(() => {
    changeBodyAttribute("data-leftbar-position", menuPosition);
  }, [menuPosition]);

  useEffect(() => {
    changeBodyAttribute("data-topbar-color", topbarTheme);
  }, [topbarTheme]);

  /**
   * Open the menu when having mobile screen
   */
  const openMenu = () => {
    setIsMenuOpened(!isMenuOpened);
    if (document.body) {
      if (isMenuOpened) {
        document.body.classList.remove("sidebar-enable");
      } else {
        document.body.classList.add("sidebar-enable");
      }
    }
  };

  return (
    <>
      <div id="wrapper">
        <Suspense fallback={loading()}>
          <Topbar
            openLeftMenuCallBack={openMenu}
            containerClass="container-fluid"
          />
        </Suspense>

        <Suspense fallback={loading()}>
          <Navbar isMenuOpened={isMenuOpened} />
        </Suspense>
        <div
          className="content-page"
          style={{
            backgroundImage: `url(${bgImage})`,
            backgroundSize: "cover",
            backgroundRepeat: "no-repeat",
          }}
        >
          <div className="content">
            <Container fluid>
              <Outlet />
            </Container>
          </div>

          <Suspense fallback={loading()}>
            <Footer />
          </Suspense>
        </div>
      </div>
    </>
  );
};

export default HorizontalLayout;
