// types
export type TableRecord = {
  id: number
  firstName: string
  lastName: string
  userName: string
}

export type ContexualTableRecord = {
  id: number
  variant?: string
  firstName: string
  lastName: string
  userName: string
}

export const records: TableRecord[] = [
  { id: 1, firstName: 'Mark', lastName: 'Otto', userName: '@mdo' },
  { id: 2, firstName: 'Jacob', lastName: 'Thornton', userName: '@fat' },
  { id: 3, firstName: 'Larry', lastName: 'The Bird', userName: '@twitter' },
]

export const stores: {
  id: number
  name: string
  city: string
  camCount: number
  status: string
  currentCustomers: number
}[] = [
  {
    id: 1,
    name: 'İstanbul Şubesi',
    city: 'İstanbul',
    camCount: 1,
    currentCustomers: 22,
    status: 'online',
  },
  {
    id: 2,
    name: 'İzmir Şubesi',
    city: 'İzmir',
    camCount: 3,
    currentCustomers: 13,
    status: 'online',
  },
  {
    id: 3,
    name: 'Ankara Şubesi',
    city: 'Ankara',
    camCount: 2,
    currentCustomers: 0,
    status: 'offline',
  },
]

export const contextualRecords: ContexualTableRecord[] = [
  {
    id: 1,
    variant: 'active',
    firstName: 'Column content',
    lastName: 'Column content',
    userName: 'Column content',
  },
  {
    id: 2,
    firstName: 'Column content',
    lastName: 'Column content',
    userName: 'Column content',
  },
  {
    id: 3,
    variant: 'success',
    firstName: 'Column content',
    lastName: 'Column content',
    userName: 'Column content',
  },
  {
    id: 4,
    firstName: 'Column content',
    lastName: 'Column content',
    userName: 'Column content',
  },
  {
    id: 5,
    variant: 'info',
    firstName: 'Column content',
    lastName: 'Column content',
    userName: 'Column content',
  },
  {
    id: 6,
    firstName: 'Column content',
    lastName: 'Column content',
    userName: 'Column content',
  },
  {
    id: 7,
    variant: 'warning',
    firstName: 'Column content',
    lastName: 'Column content',
    userName: 'Column content',
  },
  {
    id: 8,
    firstName: 'Column content',
    lastName: 'Column content',
    userName: 'Column content',
  },
  {
    id: 9,
    variant: 'danger',
    firstName: 'Column content',
    lastName: 'Column content',
    userName: 'Column content',
  },
]
