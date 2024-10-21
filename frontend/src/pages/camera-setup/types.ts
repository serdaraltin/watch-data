export type CameraItem = {
  id: string | number | undefined
  branch_id: number
  resolution: string
  install_date: string
  status: boolean
  type: string
  host: string
  label: string
  model: string
  protocol: string
  user: string
  password: string
  channel: number
  port: number
  path?: string
  aditional?: Record<string, unknown>
}

export type NewCameraItem = {
  branch_id: number
  resolution: string
  install_date: string
  status: boolean
  type: string
  host: string
  label: string
  model: string
  protocol: string
  user: string
  password: string
  channel: number
  port: number
  path?: string
  aditional?: Record<string, unknown>
}
