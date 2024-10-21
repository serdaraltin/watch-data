// hooks
import { usePageTitle } from '../../hooks'
import EditorScreen from './Editor'
import config from '../../config'
import { CameraItem } from '../camera-setup/types'
import { useNavigate } from 'react-router-dom'

const Editor = () => {
  // set pagetitle
  usePageTitle({
    title: 'Editor',
    breadCrumbItems: [
      {
        path: '/editor',
        label: 'Editor',
        active: true,
      },
    ],
  })
  const backendURL = config.BACKEND_URL
  const navigate = useNavigate()

  const handleAddCamera = async (camera: CameraItem) => {
    try {
      const response = await fetch(`${backendURL}/api/v1/camera`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(camera),
      })

      const newCamera = await response.json()
      console.log('camera request>>>>', newCamera)
    } catch (error) {
      console.error('error add cam:', error)
    }
  }

  const handleUpdateCamera = async (camera: CameraItem) => {
    try {
      const res = await fetch(`${backendURL}/api/v1/camera/:${camera.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(camera),
      })

      const data = await res.json()
      const updatedCamera = data.response
      console.log('updated cam>>>', updatedCamera)
      navigate('/camera-setup', {})
    } catch (error) {
      console.error('error on update cam:', error)
      return
    }
  }

  return (
    <>
      <EditorScreen
        handleAddCamera={handleAddCamera}
        handleUpdateCamera={handleUpdateCamera}
      />
    </>
  )
}

export default Editor
