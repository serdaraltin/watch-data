// all routes
import Routes from './routes/Routes'

// helpers
import { configureFakeBackend } from './helpers'
import { registerLocale } from 'react-datepicker'
import tr from 'date-fns/locale/tr'
// For Default import Theme.scss
import './assets/scss/Theme.scss'
import './assets/wd-assets/wd-global.scss'

const App = () => {
  registerLocale('tr', tr)
  configureFakeBackend()
  return <Routes />
}

export default App
