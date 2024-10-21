import { useState, useEffect } from 'react'
import config from '../config'

interface CustomerData {
  startTime: string
  endTime: string
  timeLabel: string
  totalCustomers: number | null
  difference: number | null
  maleCustomers: { enter: number | null; exit: number | null }
  femaleCustomers: { enter: number | null; exit: number | null }
  isCompleted: boolean | null
}

const useFilledData = (originalData: CustomerData[]): CustomerData[] => {
  const [filledData, setFilledData] = useState<CustomerData[]>([])

  const startHour = config.workingHoursStart
  const endHour = config.workingHoursEnd
  useEffect(() => {
    const fillData = () => {
      const workingHours: number[] = []
      for (let i = startHour; i < endHour; i++) {
        workingHours.push(i)
      }

      const filledDataArray: CustomerData[] = workingHours.map((hour) => {
        const formattedHour = hour < 10 ? `0${hour}` : `${hour}`
        const timeLabel = `${formattedHour}:00`

        const item = originalData.find((item) => item.timeLabel === timeLabel)
        if (item) {
          return item
        } else {
          return {
            startTime: timeLabel,
            endTime: timeLabel,
            timeLabel: timeLabel,
            totalCustomers: null,
            difference: null,
            maleCustomers: { enter: null, exit: null },
            femaleCustomers: { enter: null, exit: null },
            isCompleted: false,
          }
        }
      })

      setFilledData(filledDataArray)
    }

    fillData()
  }, [originalData, startHour, endHour])

  return filledData
}

export default useFilledData
