import DatePicker from 'react-modern-calendar-datepicker'
import { format } from 'date-fns'
import 'react-modern-calendar-datepicker/lib/DatePicker.css'
import { customFooter } from './DatePickerFooter'

// https://kiarash-z.github.io/react-modern-calendar-datepicker/
const myCustomLocale = {
  // months list by order
  months: [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
  ],

  // week days by order
  weekDays: [
    {
      name: 'Sunday', // used for accessibility
      short: 'S', // displayed at the top of days' rows
      isWeekend: true, // is it a formal weekend or not?
    },
    {
      name: 'Monday',
      short: 'M',
    },
    {
      name: 'Tuesday',
      short: 'T',
    },
    {
      name: 'Wednesday',
      short: 'W',
    },
    {
      name: 'Thursday',
      short: 'T',
    },
    {
      name: 'Friday',
      short: 'F',
    },
    {
      name: 'Saturday',
      short: 'S',
      isWeekend: true,
    },
  ],

  // just play around with this number between 0 and 6
  weekStartingIndex: 1,

  // return a { year: number, month: number, day: number } object
  getToday(gregorainTodayObject: any) {
    return gregorainTodayObject
  },

  // return a native JavaScript date here
  toNativeDate(date: any) {
    return new Date(date.year, date.month - 1, date.day)
  },

  // return a number for date's month length
  getMonthLength(date: any) {
    return new Date(date.year, date.month, 0).getDate()
  },

  // return a transformed digit to your locale
  transformDigit(digit: any) {
    return digit
  },

  // texts in the date picker
  nextMonth: 'Next Month',
  previousMonth: 'Previous Month',
  openMonthSelector: 'Open Month Selector',
  openYearSelector: 'Open Year Selector',
  closeMonthSelector: 'Close Month Selector',
  closeYearSelector: 'Close Year Selector',
  defaultPlaceholder: 'Select...',

  // for input range value
  from: 'from',
  to: 'to',

  // used for input value when multi dates are selected
  digitSeparator: ',',

  // if your provide -2 for example, year will be 2 digited
  yearLetterSkip: 0,

  // is your language rtl or ltr?
  isRtl: false,
}
type CustomDatePickerProps = {
  minimumDate?: any
  maximumDate?: any
  disabledDays?: any
  onChange: any
  value: any
  selectedDayRange: any
  shouldHighlightWeekends?: boolean
  colorPrimary?: string
  colorPrimaryLight?: string
  calendarClassName?: string
  calendarTodayClassName?: string
  calendarSelectedDayClassName?: string
  calendarRangeBetweenClassName?: string
  renderInput?: any
  wrapperClassName?: any
  inputClassName?: any
  formatInputText?: any
  inputPlaceholder?: any
  renderFooter?: any
}

export default function CustomDatePicker(props: CustomDatePickerProps) {
  return (
    <DatePicker
      {...props}
      renderFooter={customFooter}
      locale={myCustomLocale} // custom locale
    />
  )
}
