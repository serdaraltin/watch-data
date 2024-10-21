import { useState, useEffect, SetStateAction } from 'react'

interface LocalStorageOptions {
  selectedOption: 'hourly' | 'daily' | 'monthly'
  expirationTimes: {
    hourly: number
    daily: number
    monthly: number
  }
}

const useLocalStorageData = <T>(
  options: LocalStorageOptions,
  fetchData: () => Promise<{ success: boolean; Obj: T }>
) => {
  interface LocalStorageData {
    success: boolean
    Obj: T
  }

  const [data, setData] = useState<T | null>(null)
  const [isLoading, setIsLoading] = useState<boolean>(false)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    const fetchDataFromLocalStorage = () => {
      const storedData = localStorage.getItem(options.selectedOption)
      const storedTimestamp = localStorage.getItem(
        `${options.selectedOption}-timestamp`
      )
      const currentTimestamp = new Date().getTime()

      if (
        storedData &&
        storedTimestamp &&
        currentTimestamp - parseInt(storedTimestamp, 10) <
          options.expirationTimes[options.selectedOption]
      ) {
        const parsedData = JSON.parse(storedData) as LocalStorageData
        setData(parsedData.Obj)
      } else {
        fetchDataFromApi()
      }
    }

    const fetchDataFromApi = async () => {
      try {
        setIsLoading(true)
        const response = await fetchData()
        if (response.success) {
          setData(response.Obj)
          localStorage.setItem(options.selectedOption, JSON.stringify(response))
          localStorage.setItem(
            `${options.selectedOption}-timestamp`,
            new Date().getTime().toString()
          )
        } else {
          setError(new Error('API response unsuccessful'))
        }
      } catch (error) {
        setError(error as Error)
      } finally {
        setIsLoading(false)
      }
    }

    fetchDataFromLocalStorage()
  }, [options.selectedOption, options.expirationTimes, fetchData])

  return { data, isLoading, error }
}

export default useLocalStorageData
