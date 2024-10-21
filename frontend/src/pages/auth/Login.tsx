import { useEffect } from 'react'
import { Button, Alert, Row, Col } from 'react-bootstrap'
import { Navigate, Link, useLocation } from 'react-router-dom'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import { useTranslation } from 'react-i18next'

// hooks
import { useRedux } from '../../hooks/'

// actions
import { resetAuth, loginUser } from '../../redux/actions'

// components
import { VerticalForm, FormInput } from '../../components/form/'
import Loader from '../../components/Loader'

// images
import LogoDark from '../../assets/wd-assets/wd4.png'
import LogoLight from '../../assets/wd-assets/wd4.png'

import AuthLayout from './AuthLayout'

type LocationState = {
  from?: Location
}

type UserData = {
  email: string
  password: string
}

/* bottom links */
const BottomLink = () => {
  const { t } = useTranslation()

  return (
    <Row className="mt-3">
      <Col xs={12} className="text-center">
        {/* <p className="text-muted">
          <Link to="/auth/forget-password" className="text-muted ms-1">
            <i className="fa fa-lock me-1"></i>
            {t('Forgot your password?')}
          </Link>
        </p> */}
        {/* <p className="text-muted">
          {t('Hesabınız yok mu?')}{' '}
          <Link to={'/auth/register'} className="text-dark ms-1">
            <b>{t('Kayıt Ol')}</b>
          </Link>
        </p> */}
      </Col>
    </Row>
  )
}

const Login = () => {
  const { t } = useTranslation()
  const { dispatch, appSelector } = useRedux()

  const { user, userLoggedIn, loading, error } = appSelector((state) => ({
    user: state.Auth.user,
    loading: state.Auth.loading,
    error: state.Auth.error,
    userLoggedIn: state.Auth.userLoggedIn,
  }))

  useEffect(() => {
    dispatch(resetAuth())
  }, [dispatch])

  /*
    form validation schema
    */
  const schemaResolver = yupResolver(
    yup.object().shape({
      email: yup
        .string()
        .required(t('E-Posta giriniz'))
        .email(t('Geçerli bir e-Posta giriniz')),
      password: yup.string().required(t('Şifre giriniz')),
    })
  )

  /*
    handle form submission
    */
  const onSubmit = (formData: UserData) => {
    dispatch(loginUser(formData['email'], formData['password']))
  }

  const location = useLocation()
  let redirectUrl = '/'

  if (location.state) {
    const { from } = location.state as LocationState
    redirectUrl = from ? from.pathname : '/'
  }

  return (
    <>
      {userLoggedIn && user && <Navigate to={redirectUrl} replace />}

      <AuthLayout bottomLinks={<BottomLink />}>
        <div className="auth-logo mb-5">
          <Link
            to="https://www.watchdata.ai/"
            target="_blank"
            rel="noopener noreferrer"
            className="logo logo-dark text-center"
          >
            <span className="logo-lg">
              <img src={LogoDark} alt="" height="80" />
            </span>
          </Link>

          <Link
            to="https://www.watchdata.ai/"
            target="_blank"
            rel="noopener noreferrer"
            className="logo logo-light text-center"
          >
            <span className="logo-lg">
              <img src={LogoLight} alt="" height="80" />
            </span>
          </Link>
        </div>
        <div className="text-left mb-4">
          <h4 className=" mt-0">{t('Giriş Yap')}</h4>
        </div>

        {error && (
          <Alert variant="danger" className="my-2">
            {error}
          </Alert>
        )}
        {loading && <Loader />}

        <VerticalForm<UserData>
          onSubmit={onSubmit}
          resolver={schemaResolver}
          defaultValues={{
            email: 'minoa@digitales.com.tr',
            password: '',
          }}
        >
          <FormInput
            type="email"
            name="email"
            label={t('E-Posta')}
            placeholder={t('İsim@Sirketiniz.com')}
            containerClass={'mb-3'}
            style={{ borderRadius: 15 }}
          />
          <FormInput
            label={t('Şifre')}
            type="password"
            name="password"
            placeholder="Şifrenizi giriniz"
            containerClass={'mb-5'}
            style={{ borderRadius: 15 }}
          ></FormInput>

          {/* <FormInput
            type="checkbox"
            name="checkbox"
            label={t('Beni Hatırla')}
            containerClass={'mb-3'}
            defaultChecked
          /> */}

          <div className="text-center d-grid mb-3">
            <Button
              variant="primary"
              type="submit"
              disabled={loading}
              style={{ borderRadius: 15 }}
            >
              {t('Giriş Yap')}
            </Button>
          </div>
        </VerticalForm>
      </AuthLayout>
    </>
  )
}

export default Login
