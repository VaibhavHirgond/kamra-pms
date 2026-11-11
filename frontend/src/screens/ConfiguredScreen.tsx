import { ResourceScreen } from "../components/ResourceScreen"
import * as configs from "./configs"

export type ConfigName = keyof typeof configs

/** A ResourceScreen picked by config name, so the generic list screens and
 *  their configs load with the first route that needs them, not the shell. */
export default function ConfiguredScreen({ config }: { config: ConfigName }) {
  return <ResourceScreen config={configs[config]} />
}
