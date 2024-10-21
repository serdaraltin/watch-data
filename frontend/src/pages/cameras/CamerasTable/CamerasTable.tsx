import { Button, Card, Col, Dropdown, Row, Table } from 'react-bootstrap'
import { style } from 'd3'
import { CameraItem } from '../../camera-setup/types'

const CamerasTable = ({
  cameras,
  handleCams,
}: {
  cameras: CameraItem[]
  handleCams: any
}) => {
  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        width: '100%',
      }}
    >
      <Card style={{ flex: 1, margin: 15, width: '100%' }}>
        <Card.Body>
          <h4 className="header-title">Kamera Durumu</h4>

          <div className="table-responsive">
            <Table className="mb-0 text-center" variant="dark">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Kamera Adı</th>
                  <th>Türü</th>
                  <th>Modeli</th>
                  <th>Durum</th>
                </tr>
              </thead>
              <tbody>
                {(cameras || []).map((cam: CameraItem, index: number) => {
                  return (
                    <tr key={index.toString()}>
                      <th scope="row">{cam.id}</th>
                      <td>{cam.label}</td>
                      <td>{cam.type}</td>
                      <td>{cam.model}</td>
                      <td>
                        <i
                          className={
                            cam.status == true
                              ? 'fe-check-circle text-success'
                              : 'fa fa-times text-danger'
                          }
                        ></i>
                      </td>
                    </tr>
                  )
                })}
              </tbody>
            </Table>
          </div>
        </Card.Body>
      </Card>

      {/* <Button
        variant="blue"
        onClick={() => {
          handleCams()
        }}
        style={{ borderRadius: 15 }}
      >
        Kameraları Düzenle
      </Button> */}
    </div>
  )
}

export default CamerasTable
