import { Card, Dropdown, Table } from 'react-bootstrap'

// data
const cams: {
  id: number
  name: string
  type: string
  model: string
  status: boolean
}[] = []

const BranchTable = () => {
  return (
    <Card>
      <Card.Body>
        <Dropdown className="float-end" align="end">
          <Dropdown.Toggle as="a" className="cursor-pointer card-drop">
            <i className="mdi mdi-dots-vertical"></i>
          </Dropdown.Toggle>
          <Dropdown.Menu>
            {/* <Dropdown.Item>Action</Dropdown.Item>
            <Dropdown.Item>Anothther Action</Dropdown.Item>
            <Dropdown.Item>Something Else</Dropdown.Item>
            <Dropdown.Item>Separated link</Dropdown.Item> */}
          </Dropdown.Menu>
        </Dropdown>
        <h4 className="header-title">Kamera Durumu</h4>
        {/* <p className="text-muted font-14 mb-4">
          You can also invert the colors—with light text on dark backgrounds—by
          specifying <code>dark</code> attribute
        </p> */}

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
              {(cams || []).map((cam, index) => {
                return (
                  <tr key={index.toString()}>
                    <th scope="row">{cam.id}</th>
                    <td>{cam.name}</td>
                    <td>{cam.type}</td>
                    <td>{cam.model}</td>
                    <td>
                      <i
                        className={
                          cam.status === true
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
  )
}

export default BranchTable
