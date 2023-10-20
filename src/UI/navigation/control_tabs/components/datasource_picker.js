import React from "react";
import { Sources } from "../../../../common/sources";
import Select from "../../../components/input/select";

export default function DatasourcePicker({ selected, setSelected }) {
    return (
        <Select
            label="Data Source"
            value={selected}
            onChange={(val) => setSelected(parseInt(val))}
            options={Object.keys(Sources).map((source) => (
                <option key={source} value={source}>
                    {Sources[source].name}
                </option>
            ))}
        />
    );
}

export { Sources };
