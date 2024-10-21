import { Button, Card, Col, Dropdown, Modal, Row, Table } from 'react-bootstrap'
import { CameraItem } from './types'
const CameraCardItem = ({
  handleRemoveCamera,
  showUpdateCamera,
  camera,
  handleEditPoints,
}: {
  handleRemoveCamera: any
  showUpdateCamera: any
  camera: CameraItem
  handleEditPoints: any
}) => {
  return (
    <Row className="m-0">
      <Col>
        <Row>
          <Col xs={8}>
            <h5 className="mb-1">Kamera Adı: </h5>
            <p>{camera.label}</p>
          </Col>
          <Col xs={4}>
            <h5 className="mb-1">Durumu: </h5>
            <p>{camera.status === true ? 'Aktif' : 'Pasif'}</p>
          </Col>
        </Row>
        <Row>
          <Col xs={8}>
            <h5 className="mb-1">URL: </h5>
            <p>{camera.host}</p>
          </Col>
          <Col xs={4}>
            <h5 className="mb-1">PORT: </h5>
            <p>{camera.port}</p>
          </Col>
        </Row>

        <Row>
          <Col xs={8}>
            <h5 className="mb-1">PROTOKOL: </h5>
            <p>{camera.protocol}</p>
          </Col>
          <Col xs={4}>
            <h5 className="mb-1">KANAL: </h5>
            <p>{camera.channel}</p>
          </Col>
        </Row>
        <Row>
          <Col xs={8}>
            <h5 className="mb-1">MODEL: </h5>
            <p>{camera.model}</p>
          </Col>
          <Col xs={4}>
            <h5 className="mb-1">TİPİ: </h5>
            <p>{camera.type}</p>
          </Col>
        </Row>
        <Row>
          <Col xs={12} sm={8}>
            <h5 className="mb-1">KULLANICI ADI: </h5>
            <p>{camera.user}</p>
          </Col>
          <Col xs={12} sm={4}>
            <h5 className="mb-1">KURULUM: </h5>
            <p>{camera.install_date.split('T')[0]}</p>
          </Col>
        </Row>
        <Row>
          <Col xs={8}></Col>
          <Col xs={4}></Col>
        </Row>
      </Col>

      <div className="mt-4">
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            gap: 5,
          }}
        >
          <Button
            style={{
              width: '12rem',

              maxWidth: '12rem',
              borderRadius: 15,
              fontWeight: 500,
            }}
            variant="danger"
            onClick={() => handleRemoveCamera(camera.id)}
          >
            Kaldır
          </Button>
          <Button
            onClick={showUpdateCamera}
            variant="primary"
            style={{
              width: '12rem',
              maxWidth: '12rem',
              borderRadius: 15,
              fontWeight: 500,
            }}
          >
            Kamera Ayarları
          </Button>
          <Button
            onClick={() => handleEditPoints(camera)}
            variant="blue"
            style={{
              width: '12rem',
              maxWidth: '12rem',
              borderRadius: 15,
              fontWeight: 500,
            }}
          >
            Editör
          </Button>
        </div>
      </div>
    </Row>
  )
}

export default CameraCardItem
