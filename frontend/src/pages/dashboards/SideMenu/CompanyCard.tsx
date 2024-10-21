import React from 'react'
import { Card } from 'react-bootstrap'

const CompanyCard = ({ user }: { user: any }) => {
  return (
    <Card>
      {user.userImage ? (
        <img
          src={user.userImage}
          alt="user"
          className="rounded-circle mb-2 border"
          width={80}
          height={80}
          style={{ alignSelf: 'center' }}
        />
      ) : null}
      <span
        className="pro-user-name ms-1 "
        style={{
          alignSelf: 'center ',
          fontSize: 24,
          fontWeight: 500,
          color: 'white',
        }}
      >
        {user.companyName}
      </span>
    </Card>
  )
}

export default CompanyCard
