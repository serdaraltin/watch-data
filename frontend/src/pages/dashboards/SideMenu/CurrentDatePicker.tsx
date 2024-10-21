import { useEffect, useState } from "react";

import { useDispatch, useSelector } from "react-redux";

import AdmintoDatepicker from "../../../components/Datepicker";
import { setSelectedDate } from "../../../redux/actions";

function CurrentDatePicker() {
  const selectedDate = useSelector(
    (state: any) => state.Dashboard.selectedDate
  );
  const [date, setDate] = useState<Date>(selectedDate);

  const dispatch = useDispatch();

  const onDateChange = (date: Date) => {
    if (date) {
      setDate(date);
      dispatch(setSelectedDate(date));
    }
  };

  useEffect(() => {
    console.log("new day>>>>", selectedDate);
  }, [selectedDate]);

  return (
    <div className="ps-2 pe-2">
      <h6
        className="ps-1"
        style={{
          fontSize: 16,
        }}
      >
        Gösterilen Gün:
      </h6>
      <AdmintoDatepicker
        showTimeSelect={false}
        dateFormat="dd-MM-yyyy"
        value={date}
        onChange={(date: Date) => {
          onDateChange(date);
        }}
        locale="tr"
      />
    </div>
  );
}

export default CurrentDatePicker;
