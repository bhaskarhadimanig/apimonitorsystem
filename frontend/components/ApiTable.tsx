import { Table, TableHead, TableRow, TableCell, TableBody, IconButton } from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import Link from "next/link";

export default function ApiTable({ apis }) {
  return (
    <Table>
      <TableHead>
        <TableRow>
          <TableCell>API Name</TableCell>
          <TableCell>URL</TableCell>
          <TableCell>Frequency (sec)</TableCell>
          <TableCell>Status</TableCell>
          <TableCell>Actions</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {apis.map((api: any) => (
          <TableRow key={api.id}>
            <TableCell>{api.name}</TableCell>
            <TableCell>{api.url}</TableCell>
            <TableCell>{api.frequency}</TableCell>
            <TableCell>{api.last_status || "-"}</TableCell>
            <TableCell>
              <Link href={`/apis/${api.id}`}>
                <IconButton><EditIcon /></IconButton>
              </Link>
              <IconButton><DeleteIcon /></IconButton>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}