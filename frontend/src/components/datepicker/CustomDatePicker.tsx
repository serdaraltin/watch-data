import React, { useState } from 'react'
import 'react-modern-calendar-datepicker/lib/DatePicker.css'
import CustomDatePicker from './CustomDatePickerItem'

const DatePicker = () => {
  const [selectedDayRange, setSelectedDayRange] = useState({
    from: null,
    to: null,
  })
  return (
    <CustomDatePicker
      value={selectedDayRange}
      onChange={setSelectedDayRange}
      inputPlaceholder="Select a day range"
      shouldHighlightWeekends
      selectedDayRange={selectedDayRange}
    />
  )
}

export default DatePicker
