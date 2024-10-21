import { Button, Card, Col, Dropdown, Modal, Row, Table } from 'react-bootstrap'
import * as yup from 'yup'
import { NewCameraItem } from './types'
import { FormInput } from '../../components/form'

import { useState } from 'react'

const validationSchema = yup.object().shape({
  label: yup.string().required('Kamera Adı gereklidir'),
  host: yup.string().required('URL gereklidir'),
  port: yup
    .number()
    .required('PORT gereklidir')
    .min(1, 'PORT en az 1 olmalıdır')
    .max(65535, 'PORT en fazla 65535 olmalıdır'),
  model: yup.string().required('Modeli gereklidir'),
  type: yup.string().required('Tipi gereklidir'),
  protocol: yup.string().required('Protokol gereklidir'),
  resolution: yup.string().required('Çözünürlük gereklidir'),
  channel: yup
    .number()
    .required('Kanal gereklidir')
    .min(1, 'Kanal en az 1 olmalıdır')
    .max(32, 'Kanal en fazla 32 olmalıdır'),
  user: yup.string().required('Kamera Kullanıcı Adı gereklidir'),
  password: yup.string().required('Kamera Kullanıcı Şifresi gereklidir'),
})

const NewCameraModal = ({
  isAddCameraOpen,
  hideAddCamera,
  handleInputChange,
  newCamera,
  handleAddOperation,
}: {
  isAddCameraOpen: boolean
  hideAddCamera: any
  handleInputChange: any
  handleAddOperation: any
  newCamera: NewCameraItem
}) => {
  const [errors, setErrors] = useState({})

  const validateForm = async () => {
    try {
      await validationSchema.validate(newCamera, { abortEarly: false })
      setErrors({})
      return true
    } catch (validationErrors: any) {
      const newErrors: { [key: string]: string } = {}
      validationErrors.inner.forEach((error: any) => {
        newErrors[error.path] = error.message
      })
      setErrors(newErrors)
      return false
    }
  }

  const handleSubmit = async () => {
    const isValid = await validateForm()
    console.log('isValid new camera form>>>', isValid, 'errors>>>>', errors)
    if (isValid) {
      handleAddOperation(newCamera)
    }
  }

  return (
    <Modal show={isAddCameraOpen} onHide={hideAddCamera} centered>
      <Row className="m-0 p-5">
        <Col>
          <FormInput
            className="mb-3"
            name="label"
            label="Kamera Adı:"
            type="text"
            value={newCamera.label}
            onChange={(event) => handleInputChange(event)}
          />
          <Row>
            <Col xl={8}>
              <FormInput
                className="mb-3"
                name="host"
                label="URL:"
                type="text"
                value={newCamera.host}
                onChange={(event) => handleInputChange(event)}
              />
            </Col>
            <Col xl={4}>
              <FormInput
                className="mb-3"
                name="port"
                label="PORT:"
                type="number"
                min={1}
                max={65535}
                value={newCamera.port}
                onChange={(event) => handleInputChange(event)}
              />
            </Col>
          </Row>
          <FormInput
            className="mb-3"
            name="model"
            label="Modeli:"
            type="text"
            value={newCamera.model}
            onChange={(event) => handleInputChange(event)}
          />
          <Row>
            <Col xl={6}>
              <FormInput
                className="mb-3"
                name="type"
                label="Tipi:"
                type="select"
                value={newCamera.type}
                onChange={(event) => handleInputChange(event)}
              >
                <option value="Analog">Analog</option>
                <option value="Digital">Digital</option>
              </FormInput>
            </Col>
            <Col xl={6}>
              <FormInput
                className="mb-3"
                name="protocol"
                label="Protokol"
                type="select"
                value={newCamera.protocol}
                onChange={(event) => handleInputChange(event)}
              >
                <option value="RTSP">RTSP</option>
                <option value="HTTP">HTTP</option>
                <option value="FTP">FTP</option>
                <option value="TCP">TCP</option>
                <option value="POP3">POP3</option>
                <option value="ICMP">ICMP</option>
                <option value="SNMP">SNMP</option>
              </FormInput>
            </Col>
          </Row>
          <Row>
            <Col xl={8}>
              <FormInput
                className="mb-3"
                name="resolution"
                label="Çözünürlük"
                type="select"
                value={newCamera.resolution}
                onChange={(event) => handleInputChange(event)}
              >
                <option value="SD">SD</option>
                <option value="HD">HD</option>
                <option value="FHD">FHD</option>
              </FormInput>
            </Col>
            <Col xl={4}>
              <FormInput
                className="mb-3"
                name="channel"
                label="Kanal:"
                type="number"
                min={1}
                max={32}
                value={newCamera.channel}
                onChange={(event) => handleInputChange(event)}
              />
            </Col>
          </Row>

          <FormInput
            className="mb-3"
            name="user"
            label="Kamera Kullanıcı Adı:"
            type="text"
            value={newCamera.user}
            onChange={(event) => handleInputChange(event)}
          />
          <FormInput
            className="mb-3"
            name="password"
            label="Kamera Kullanıcı Şifresi:"
            type="text"
            value={newCamera.password}
            onChange={(event) => handleInputChange(event)}
          />
          <FormInput
            className="mb-3"
            name="path"
            label="Yayın Adresi:"
            type="text"
            value={newCamera.path}
            onChange={(event) => handleInputChange(event)}
          />

          <Row>
            <Button
              style={{
                flex: 1,
                maxWidth: '12rem',
                borderRadius: 15,
                fontWeight: 500,
                margin: 10,
              }}
              variant="danger"
              onClick={() => {
                hideAddCamera()
              }}
            >
              İptal
            </Button>

            <Button
              style={{
                flex: 1,
                maxWidth: '12rem',
                borderRadius: 15,
                fontWeight: 500,
                margin: 10,
              }}
              variant="blue"
              onClick={handleSubmit}
              // disabled={Object.keys(errors).length > 0}
            >
              Devam Et
            </Button>
          </Row>
        </Col>
      </Row>
    </Modal>
  )
}

export default NewCameraModal
{
  /* <FormInput
            className="mb-3"
            name="install_date"
            label="Kamera Kurulum Tarihi:"
            type="text"
            value={newCamera.install_date.split('T')[0]}
            onChange={(event) => handleInputChange(event)}
          /> */
}
