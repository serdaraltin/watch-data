import { useEffect } from 'react'
import { Row, Col } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { useTranslation } from 'react-i18next'

// hooks
import { useRedux } from '../../hooks/'

//actions
import { logoutUser, resetAuth } from '../../redux/actions'

// components
import AuthLayout from './AuthLayout'

// images
import LogoDark from '../../assets/wd-assets/wd4.png'
import LogoLight from '../../assets/wd-assets/wd4.png'

const LogoutIcon = () => {
  return (
    <svg
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 130.2 130.2"
    >
      <circle
        className="path circle"
        fill="none"
        stroke="#4bd396"
        strokeWidth="6"
        strokeMiterlimit="10"
        cx="65.1"
        cy="65.1"
        r="62.1"
      />
      <polyline
        className="path check"
        fill="none"
        stroke="#4bd396"
        strokeWidth="6"
        strokeLinecap="round"
        strokeMiterlimit="10"
        points="100.2,40.2 51.5,88.8 29.8,67.5 "
      />
    </svg>
  )
}

/* bottom link */
const BottomLink = () => {
  const { t } = useTranslation()
  return (
    <Row className="mt-3">
      <Col xs={12} className="text-center">
        <p className="text-muted">
          <Link to={'/auth/login'} className="text-dark ms-1">
            <b>{t('Giriş Yap')}</b>
          </Link>
        </p>
      </Col>
    </Row>
  )
}

const Logout = () => {
  const { t } = useTranslation()
  const { dispatch } = useRedux()

  useEffect(() => {
    dispatch(resetAuth())
  }, [dispatch])

  useEffect(() => {
    dispatch(logoutUser())
  }, [dispatch])

  return (
    <AuthLayout hasLogo={false} bottomLinks={<BottomLink />}>
      <div className="text-center w-75 m-auto">
        <div className="auth-logo">
          <Link to="/" className="logo logo-dark text-center">
            <span className="logo-lg">
              <img src={LogoDark} alt="" height="100" />
            </span>
          </Link>

          <Link to="/" className="logo logo-light text-center">
            <span className="logo-lg">
              <img src={LogoLight} alt="" height="100" />
            </span>
          </Link>
        </div>
      </div>
      <div className="text-center">
        <div className="mt-4">
          <div className="logout-checkmark">
            <LogoutIcon />
          </div>
        </div>

        {/* <h3>{t('Görüşürüz!')}</h3> */}

        <h3 className="text-muted"> {t('Başarıyla çıkış yaptınız.')} </h3>
      </div>
    </AuthLayout>
  )
}

export default Logout
