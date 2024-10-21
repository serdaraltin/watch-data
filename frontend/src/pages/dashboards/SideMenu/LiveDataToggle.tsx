import { FormCheck } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { setIsCurrentDataShowing } from "../../../redux/actions";

const LiveDataToggle = () => {
  const isCurrentDataShowing = useSelector(
    (state: any) => state.Dashboard.isCurrentDataShowing
  );
  const dispatch = useDispatch();

  const handleDataVisibilityChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    dispatch(setIsCurrentDataShowing(event.target.checked));
  };

  return (
    <div
      style={{
        display: "flex",
        padding: "0.5rem 0px",
        margin: "10px 0 30px 20px",
      }}
    >
      <FormCheck
        type="switch"
        id="data-visibility-switch"
        checked={isCurrentDataShowing}
        onChange={handleDataVisibilityChange}
      />
      <span style={{ marginRight: " 0.5rem " }}>
        {isCurrentDataShowing ? "Anlık Veriyi Gizle" : "Anlık Veriyi Göster"}
      </span>
    </div>
  );
};

export default LiveDataToggle;
