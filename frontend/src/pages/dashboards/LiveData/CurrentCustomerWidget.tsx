import { useSelector } from "react-redux";

// component
import CurrentCustomersStatisticsWidget from "../../../components/CurrentCustomersStatisticsWidget";

const CurrentCustomersWidget = ({
  yesterdayTotalCustomers,
}: {
  yesterdayTotalCustomers: any;
}) => {
  const currentCustomers = useSelector(
    (state: any) => state.Dashboard.currentCustomers
  );

  const yesterdayCount = yesterdayTotalCustomers?.count ?? 0;
  const trendValue =
    yesterdayCount !== 0
      ? ((currentCustomers?.count ?? 0 - yesterdayCount) / yesterdayCount) * 100
      : 0;

  const ratio =
    (currentCustomers?.count / (yesterdayCount > 0 ? yesterdayCount : 1)) * 100;

  return (
    <>
      <CurrentCustomersStatisticsWidget
        variant={
          (currentCustomers?.count ?? 0 - yesterdayCount) / yesterdayCount >= 0
            ? "success"
            : "danger"
        }
        title="Bugünkü Müşteri Sayısı"
        trendValue={`${trendValue.toFixed(2)}%`}
        trendIcon={
          (currentCustomers?.count ?? 0 - yesterdayCount) / yesterdayCount >= 0
            ? "mdi mdi-trending-up"
            : "mdi mdi-trending-down"
        }
        ratio={ratio}
        stats={
          currentCustomers?.count
            ? //currentCustomers.current_number_of_people > 0
              currentCustomers?.count
            : 0
        }
        // subTitle="-"
        subTitle="Dünkü Toplam Müşteri"
        progress={currentCustomers?.count ?? 0}
        subStats={yesterdayCount}
      />
    </>
  );
};

export default CurrentCustomersWidget;
