import { Button, Card, Container } from 'react-bootstrap'
import Scrollbar from '../../components/Scrollbar'
import { usePageTitle } from '../../hooks'
// import { notifications } from '../../layouts/Topbar/data'

const Notifications = () => {
  usePageTitle({
    title: 'Notifications',
    breadCrumbItems: [],
  })
  const notifications: any[] = []
  return (
    <>
      <Card style={{ marginTop: 30 }}>
        <Container>
          <h3 className="text-center m-3">Tüm Bildirimleriniz</h3>
          <Container>
            {notifications.length > 0 ? (
              <Scrollbar style={{ height: '70vh' }}>
                {(notifications || []).map((item, index) => {
                  // item.path&& notification item will be a link to file else will be button
                  return item.path ? (
                    <a
                      key={index.toString()}
                      className="notify-item w-100 mb-2 btn btn-light"
                      href={item.path}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <>
                        <p className="notify-details mb-1 mt-2">{item.text}</p>
                        <p className="text-muted m-0">{item.subText}</p>
                        <div
                          style={{
                            display: 'flex',
                            justifyContent: 'space-between',
                          }}
                        >
                          <small className="text-muted">{item.type}</small>
                          <small className="text-muted">{item.date}</small>
                        </div>
                      </>
                    </a>
                  ) : (
                    <Button
                      key={index.toString()}
                      className="notify-item w-100 mb-2 btn btn-light"
                    >
                      <>
                        <p className="notify-details mb-1 mt-2">{item.text}</p>
                        <p className="text-muted m-0">{item.subText}</p>
                        <div
                          style={{
                            display: 'flex',
                            justifyContent: 'space-between',
                          }}
                        >
                          <small className="text-muted">{item.type}</small>
                          <small className="text-muted">{item.date}</small>
                        </div>
                      </>
                    </Button>
                  )
                })}
              </Scrollbar>
            ) : (
              <p style={{ textAlign: 'center', margin: 100 }}>
                Henüz bir bildiriminiz yok.
              </p>
            )}
          </Container>
        </Container>
      </Card>
    </>
  )
}

export default Notifications
