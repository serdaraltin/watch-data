import { Badge, Dropdown } from 'react-bootstrap'
import { Link } from 'react-router-dom'
// import classNames from 'classnames'

// hooks
import { useToggle } from '../../hooks'

// components
import Scrollbar from '../Scrollbar'

// dummy data
import { Notification } from '../../layouts/types'
import { useState } from 'react'

type NotificationDropdownProps = {
  notifications: Notification[]
}

const NotificationDropdown = ({ notifications }: NotificationDropdownProps) => {
  const [isOpen, show, hide] = useToggle()
  const [notificationCount, setNotificationCount] = useState(0)

  const toggleDropdown = () => {
    isOpen ? hide() : show()
  }

  const handleClearNotification = () => {
    console.log('Bildirimler temizlendi!')
    setNotificationCount(0)
  }

  return (
    <Dropdown show={isOpen} onToggle={toggleDropdown}>
      <Dropdown.Toggle
        variant=""
        as="a"
        className="nav-link waves-effect waves-light"
        onClick={toggleDropdown}
      >
        <i className="fe-bell noti-icon"></i>
        {notificationCount > 0 ? (
          <Badge bg="danger" className="rounded-circle noti-icon-badge">
            {notificationCount}
          </Badge>
        ) : null}
      </Dropdown.Toggle>

      <Dropdown.Menu align="end" className="dropdown-lg">
        <div onClick={toggleDropdown}>
          <Dropdown.Item as="div" className="noti-title">
            <h5 className="m-0">
              <span className="float-end">
                <Link
                  to="#"
                  onClick={handleClearNotification}
                  className="text-dark"
                >
                  <small>Temizle</small>
                </Link>
              </span>
              Bildirimler
            </h5>
          </Dropdown.Item>
          <Scrollbar className="noti-scroll">
            {(notifications || []).map((item, index) => {
              return (
                <Dropdown.Item key={index.toString()} className="notify-item">
                  {item.avatar ? (
                    <>
                      <div className="notify-icon">
                        <img
                          src={item.avatar}
                          alt=""
                          className="img-fluid rounded-circle"
                        />
                      </div>
                      <p className="notify-details">{item.text}</p>
                      <p className="text-muted mb-0 user-msg">
                        <small>{item.subText}</small>
                      </p>
                    </>
                  ) : (
                    <>
                      {/* <div
                        className={classNames(
                          'notify-icon',
                          'bg-' + item.bgColor
                        )}
                      >
                        <i className={item.icon}></i>
                      </div> */}
                      <p className="notify-details">
                        {item.text}{' '}
                        <small className="text-muted">{item.subText}</small>
                      </p>
                    </>
                  )}
                </Dropdown.Item>
              )
            })}
          </Scrollbar>

          <Dropdown.Item className="text-center text-primary notify-item notify-all">
            <Link to="/notifications" onClick={handleClearNotification}>
              Hepsini Gör<i className="fe-arrow-right"></i>
            </Link>
          </Dropdown.Item>
        </div>
      </Dropdown.Menu>
    </Dropdown>
  )
}

export default NotificationDropdown
