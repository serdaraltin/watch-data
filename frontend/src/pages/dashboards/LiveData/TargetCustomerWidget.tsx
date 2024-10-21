// component
import StatisticsWidget1 from "../../../components/StatisticsWidget1";
import config from "../../../config";
import { formatDate } from "../../../utils/helpers";
import { useEffect, useState } from "react";
import { useSelector } from "react-redux";

const TargetCustomersWidget = () => {
  const targetHourlyCustomers = config.targetHourlyCustomers;
  const [currentCustomers, setCurrentCustomers] = useState({
    current_customer: 0,
  });

  const refreshTime = useSelector((state: any) => state.Dashboard.refreshTime);

  //for requests
  let startDate = new Date();
  startDate.setHours(config.workingHoursStart, 0, 0, 0);
  let start_date = formatDate(startDate);

  let endDate = new Date();
  endDate.setHours(config.workingHoursEnd, 0, 0, 0);
  let end_date = formatDate(endDate);

  //endpoint urls
  let endpointCount = `${config.SERVICE_URL}/api/data/current_customer`;

  const fetchCamsData = async () => {
    let body = {
      branch_id: config.branchId,
      camera_id: config.entranceCam,
      between: {
        start_date: start_date,
        end_date: end_date,
      },
    };
    let dataCount;
    try {
      const responseCount = await fetch(endpointCount, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });

      if (!responseCount.ok) {
        throw new Error(`http error! status: ${responseCount.status}`);
      }

      dataCount = await responseCount.json();
      setCurrentCustomers(dataCount?.message);
    } catch (error) {
      console.error("error fetch data currentcustomers :", error);
    }
  };

  useEffect(() => {
    fetchCamsData();
    const intervalId = setInterval(() => {
      // console.log(`fetching charts data ${refreshTime} ms period`);
      fetchCamsData();
    }, refreshTime);
    return () => {
      clearInterval(intervalId);
    };
  }, [refreshTime]);

  // useEffect(() => {
  //   console.log(">>>", currentCustomers);
  // }, [currentCustomers]);

  return (
    <>
      <StatisticsWidget1
        title="Hedefe Göre Anlık Müşteri Yüzdesi"
        data={Math.floor(
          ((currentCustomers?.current_customer ?? 0) / targetHourlyCustomers) *
            100
        )}
        stats={parseFloat(
          (
            (currentCustomers?.current_customer ?? 0) / targetHourlyCustomers
          ).toFixed(2)
        )}
        subStats={targetHourlyCustomers}
        color={"#00a0d0"}
        subTitle="Hedef Müşteri Sayısı"
      />
    </>
  );
};

export default TargetCustomersWidget;
