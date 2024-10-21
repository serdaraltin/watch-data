import { Button, Card, Col, Dropdown, Modal, Row, Table } from 'react-bootstrap'
import { CameraItem } from './types'
import { FormInput } from '../../components/form'
import { useState } from 'react'
import * as Yup from 'yup'

const validationSchema = Yup.object().shape({
  label: Yup.string().required('Kamera Adı boş bırakılamaz'),
  host: Yup.string()
    .url('Geçerli bir URL girin')
    .required('URL boş bırakılamaz'),
  port: Yup.number()
    .required('PORT boş bırakılamaz')
    .positive('Negatif sayılar kullanılamaz'),
  model: Yup.string().required('Model boş bırakılamaz'),
  type: Yup.string().required('Tipi boş bırakılamaz'),
  protocol: Yup.string().required('Protokol boş bırakılamaz'),
  resolution: Yup.string().required('Çözünürlük boş bırakılamaz'),
  channel: Yup.number()
    .required('Kanal boş bırakılamaz')
    .min(1, 'En az 1 olmalıdır')
    .max(32, 'En fazla 32 olabilir'),
  user: Yup.string().required('Kamera Kullanıcı Adı boş bırakılamaz'),
  password: Yup.string().required('Kamera Kullanıcı Şifresi boş bırakılamaz'),
  path: Yup.string().required('Yayın Adresi boş bırakılamaz'),
})

const UpdateCameraModal = ({
  handleUpdateCamera,
  isUpdateCameraOpen,
  hideUpdateCamera,
  handleInputChange,
  camera,
  index,
}: {
  handleUpdateCamera: any
  isUpdateCameraOpen: boolean
  hideUpdateCamera: any
  handleInputChange: any
  camera: CameraItem
  index: any
}) => {
  const [formData, setFormData] = useState({
    label: camera.label || '',
    host: camera.host || '',
    port: camera.port || '',
    model: camera.model || '',
    type: camera.type || '',
    protocol: camera.protocol || '',
    resolution: camera.resolution || '',
    channel: camera.channel || '',
    user: camera.user || '',
    password: camera.password || '',
    path: camera.path || '',
  })

  const [errors, setErrors] = useState({
    label: '',
    host: '',
    port: '',
    model: '',
    type: '',
    protocol: '',
    resolution: '',
    channel: '',
    user: '',
    password: '',
    path: '',
  })
  const handleBlur = (fieldName: string) => {
    validationSchema
      .validateAt(fieldName, formData)
      .then(() => setErrors({ ...errors, [fieldName]: '' }))
      .catch((error) => setErrors({ ...errors, [fieldName]: error.message }))
  }

  const handleSubmit = () => {
    validationSchema
      .validate(formData, { abortEarly: false })
      .then(() => {
        // Form is valid, proceed with submission
        handleUpdateCamera(formData)
      })
      .catch((validationErrors) => {
        const newErrors: any = {}
        validationErrors.inner.forEach(
          (error: { path: string | number; message: any }) => {
            newErrors[error.path] = error.message
          }
        )
        setErrors(newErrors)
      })
  }
  return (
    <Modal show={isUpdateCameraOpen} onHide={hideUpdateCamera} centered>
      <Row className="m-0 p-5">
        <Col>
          <FormInput
            className="mb-3"
            name="label"
            label="Kamera Adı:"
            type="text"
            value={camera.label}
            onChange={(event) => handleInputChange(event, index)}
          />
          <Row>
            <Col xl={8}>
              <FormInput
                className="mb-3"
                name="host"
                label="URL:"
                type="text"
                value={camera.host}
                onChange={(event) => handleInputChange(event, index)}
              />
            </Col>
            <Col xl={4}>
              <FormInput
                className="mb-3"
                name="port"
                label="PORT:"
                type="number"
                value={camera.port}
                onChange={(event) => handleInputChange(event, index)}
              />
            </Col>
          </Row>
          <FormInput
            className="mb-3"
            name="model"
            label="Modeli:"
            type="text"
            value={camera.model}
            onChange={(event) => handleInputChange(event, index)}
          />
          <Row>
            <Col xl={6}>
              <FormInput
                className="mb-3"
                name="type"
                label="Tipi:"
                type="select"
                value={camera.type}
                onChange={(event) => handleInputChange(event, index)}
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
                value={camera.protocol}
                onChange={(event) => handleInputChange(event, index)}
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
            <Row>
              <Col xl={8}>
                <FormInput
                  className="mb-3"
                  name="resolution"
                  label="Çözünürlük"
                  type="select"
                  value={camera.resolution}
                  onChange={(event) => handleInputChange(event, index)}
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
                  value={camera.channel}
                  onChange={(event) => handleInputChange(event, index)}
                />
              </Col>
            </Row>
          </Row>
          <FormInput
            className="mb-3"
            name="user"
            label="Kamera Kullanıcı Adı:"
            type="text"
            value={camera.user}
            onChange={(event) => handleInputChange(event, index)}
          />
          <FormInput
            className="mb-3"
            name="password"
            label="Kamera Kullanıcı Şifresi:"
            type="text"
            value={camera.password}
            onChange={(event) => handleInputChange(event, index)}
          />
          <FormInput
            className="mb-3"
            name="path"
            label="Yayın Adresi:"
            type="text"
            value={camera.path}
            onChange={(event) => handleInputChange(event, index)}
          />
          {/* <FormInput
            className="mb-3"
            name="install_date"
            label="Kamera Kurulum Tarihi:"
            type="text"
            value={camera.install_date.split('T')[0]}
            onChange={(event) => handleInputChange(event, index)}
          /> */}
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
                hideUpdateCamera()
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
              disabled={Object.values(errors).some((error) => !!error)}
            >
              Kaydet
            </Button>
          </Row>
        </Col>
      </Row>
    </Modal>
  )
}

export default UpdateCameraModal
