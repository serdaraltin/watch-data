import { Button, Col, Container, Row } from 'react-bootstrap'
import { usePageTitle } from '../../hooks'
import { FormInput } from '../../components/form'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

const Settings = () => {
  const [openHour, setOpenHour] = useState('10:00')
  const [closeHour, setCloseHour] = useState('22:00')
  usePageTitle({
    title: 'Ayarlar',
    breadCrumbItems: [],
  })
  const handleSave = () => {
    console.log(
      'ayarlar kaydedildi. openHour:',
      openHour,
      ' closeHour:',
      closeHour
    )
  }
  //   useEffect(() => {
  //     console.log('openHour:', openHour, ' closeHour:', closeHour)
  //   }, [openHour, closeHour])

  return (
    <>
      <Container>
        <h2 className="text-center m-3">Ayarlar</h2>
        <Container>
          <h4 className=" mb-3">Çalışma Saatleri</h4>
          <Row>
            <Col xs={6}>
              <FormInput
                name="select"
                label="Açılış Saati:"
                type="select"
                containerClass="mb-1 w-100"
                className="form-select "
                key="select"
                onChange={(e) => setOpenHour(e.target.value)}
                value={openHour}
              >
                <option value="07:00">07:00</option>
                <option value="08:00">08:00</option>
                <option value="09:00">09:00</option>
                <option value="10:00">10:00</option>
                <option value="11:00">11:00</option>
                <option value="12:00">12:00</option>
                <option value="13:00">13:00</option>
                <option value="14:00">14:00</option>
                <option value="15:00">15:00</option>
                <option value="16:00">16:00</option>
                <option value="17:00">17:00</option>
                <option value="18:00">18:00</option>
                <option value="19:00">19:00</option>
                <option value="20:00">20:00</option>
                <option value="21:00">21:00</option>
                <option value="22:00">22:00</option>
                <option value="23:00">23:00</option>
                <option value="24:00">24:00</option>
              </FormInput>
            </Col>
            <Col xs={6}>
              <FormInput
                name="select"
                label="Kapanış Saati:"
                type="select"
                containerClass="mb-1 w-100"
                className="form-select"
                key="select"
                onChange={(e) => setCloseHour(e.target.value)}
                value={closeHour}
              >
                <option value="07:00">07:00</option>
                <option value="08:00">08:00</option>
                <option value="09:00">09:00</option>
                <option value="10:00">10:00</option>
                <option value="11:00">11:00</option>
                <option value="12:00">12:00</option>
                <option value="13:00">13:00</option>
                <option value="14:00">14:00</option>
                <option value="15:00">15:00</option>
                <option value="16:00">16:00</option>
                <option value="17:00">17:00</option>
                <option value="18:00">18:00</option>
                <option value="19:00">19:00</option>
                <option value="20:00">20:00</option>
                <option value="21:00">21:00</option>
                <option value="22:00">22:00</option>
                <option value="23:00">23:00</option>
                <option value="24:00">24:00</option>
              </FormInput>
            </Col>
          </Row>
          <Row className="mb-5 mt-5">
            <Link
              style={{
                fontSize: 18,
                width: '100vw',
              }}
              to={'/camera-setup'}
            >
              Kamera Kurulumu
            </Link>
          </Row>
          <Row style={{ alignItems: 'center', justifyContent: 'center' }}>
            <Col
              style={{
                fontSize: 20,
                width: '100vw',
                alignItems: 'center',
                justifyContent: 'center',
                display: 'flex',
              }}
            >
              <Button
                onClick={handleSave}
                className="mt-5"
                style={{ width: '18rem' }}
              >
                Kaydet
              </Button>
            </Col>
          </Row>
        </Container>
      </Container>
    </>
  )
}

export default Settings
